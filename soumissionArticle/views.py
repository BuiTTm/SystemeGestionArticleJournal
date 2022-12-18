from http.client import HTTPResponse
from django.shortcuts import render
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
            if request.POST['title']:
                return render(request, 'journal/home.html')
            else:
                return render(request, 'journal/home.html')
    else:
        return HTTPResponse('Unauthorized', status=401)
