from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.forms import modelform_factory, Textarea
from .models import Article


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
        ArticleFormSet = modelform_factory(
            Article, fields=(
                'titre', 'description', 'auteurs_secondaires', 'categorie'),
            widgets={
                'titre': Textarea(attrs={'cols': 80, 'rows': 2}),
                'description': Textarea(attrs={'cols': 80, 'rows': 4}),
                'auteurs_secondaires': Textarea(attrs={'cols': 80, 'rows': 2}),
            })
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
