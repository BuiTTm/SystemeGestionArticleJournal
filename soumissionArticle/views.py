from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.forms import modelform_factory, Textarea
from django.http import HttpResponseNotFound
from .models import Article, SoumissionArticle, Comite, Commentaire
from .utils import handle_soumission_article_file_upload


ArticleFormSet = modelform_factory(
    Article, fields=(
        'titre', 'description', 'auteurs_secondaires', 'categorie'),
    widgets={
        'titre': Textarea(attrs={'cols': 80, 'rows': 2}),
        'description': Textarea(attrs={'cols': 80, 'rows': 4}),
        'auteurs_secondaires': Textarea(attrs={'cols': 80, 'rows': 2}),
    })


def home(request):
    return render(request, 'journal/home.html')


def articles(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            articles_list = Article.objects.filter(auteur_id=request.user.id)
            context = {
                'articles': articles_list,
            }
            return render(request, 'articles/list.html', context)
    else:
        return HTTPResponse('Unauthorized', status=401)


def articles_new(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            formset = ArticleFormSet(request.POST)
            if formset.is_valid():
                new_article = formset.save(commit=False)
                new_article.auteur_id = request.user.id
                new_article.save()
                return redirect('/articles')
        else:
            formset = ArticleFormSet()
        return render(request, 'articles/new.html', {'formset': formset})
    else:
        return HTTPResponse('Unauthorized', status=401)


def article(request, article_id):
    if request.user.is_authenticated:
        article_single = Article.objects.get(id=article_id)
        if article_single is None:
            return HttpResponseNotFound("L'article n'a pas été trouvé.")

        if request.method == 'POST':
            if request.FILES and request.FILES['soumission']:
                soumission_article = SoumissionArticle(article_id=article_id)
                soumission_article.save()

                filename = f"soumission-{soumission_article.id}.pdf"

                handle_soumission_article_file_upload(
                    request.FILES['soumission'],
                    filename
                )

                soumission_article.lien = f"/static/uploads/{filename}"
                soumission_article.save()

                formset = ArticleFormSet(instance=article_single)
            else:
                formset = ArticleFormSet(request.POST, instance=article_single)
                if formset.is_valid():
                    formset.save()
                    return redirect('/articles')
        else:
            formset = ArticleFormSet(instance=article_single)

        soumission_articles = SoumissionArticle.objects.filter(
            article_id=article_id).order_by('-created')
        return render(request, 'articles/single.html', {
            'formset': formset,
            'soumissions': soumission_articles
        })
    else:
        return HTTPResponse('Unauthorized', status=401)


def evaluations(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            comite_list = Comite.objects.filter(evaluateurs=request.user.id)
            context = {
                'comites': comite_list,
            }
            return render(request, 'evaluateurs/list.html', context)
    else:
        return HTTPResponse('Unauthorized', status=401)


def evaluation(request, evaluation_id):
    if request.user.is_authenticated:
        evaluation_single = Comite.objects.get(id=evaluation_id)
        if evaluation_single is None:
            return HttpResponseNotFound("Le comité n'a pas été trouvé.")

        soumission_articles = SoumissionArticle.objects.filter(
            article_id=evaluation_single.article_id).order_by('-created')
        if request.method == 'POST' and soumission_articles.count() > 0:
            comment_text = request.POST['comment']
            commentaire = Commentaire(
                text=comment_text,
                comite_id=evaluation_id,
                evaluateur_id=request.user.id,
                soumission_id=soumission_articles[0].id
            )
            commentaire.save()

        commentaires = Commentaire.objects.filter(comite_id=evaluation_id).order_by('-created')
        return render(request, 'evaluateurs/single.html', {
            'article': evaluation_single.article,
            'soumissions': soumission_articles,
            'commentaires': commentaires
        })
    else:
        return HTTPResponse('Unauthorized', status=401)
