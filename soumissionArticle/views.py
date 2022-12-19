from http.client import HTTPResponse
from django.shortcuts import render
from django.forms import modelform_factory, Textarea
from .models import Article, ArticleAuteur

def home(request):
    return render(request, 'journal/home.html')

def articles(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            articles_auteurs = ArticleAuteur.objects.filter(auteur_principal_id=request.user.id)
            ids = map(lambda x: x.id, articles_auteurs)
                
            articles = Article.objects.filter(auteur_id__in=ids)
            context = {
                'articles': articles,
            }
            return render(request, 'articles/list.html', context)
    else:
        return HTTPResponse('Unauthorized', status=401)

def articles_new(request):
    if request.user.is_authenticated:
        ArticleFormSet = modelform_factory(
            Article, fields=('titre', 'description', 'categorie'),
            widgets={'titre': Textarea(attrs={'cols': 80, 'rows': 2}), 'description': Textarea(attrs={'cols': 80, 'rows': 4})})
        if request.method == 'POST':
            formset = ArticleFormSet(request.POST)
            if formset.is_valid():
                new_article = formset.save(commit=False)
                article_auteur = ArticleAuteur(auteur_principal_id=request.user.id)
                article_auteur.save()
                
                new_article.auteur_id = article_auteur.id
                formset.save()
                # do something.
        else:
            formset = ArticleFormSet()
        return render(request, 'articles/new.html', {'formset': formset})
    else:
        return HTTPResponse('Unauthorized', status=401)
