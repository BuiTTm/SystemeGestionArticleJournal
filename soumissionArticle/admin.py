from django.contrib import admin
from .models import SoumissionArticle, Article


class SoumissionArticleInline(admin.StackedInline):
    model = SoumissionArticle
    readonly_fields = ['lien']
    extra = 0


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['titre', 'statut', 'auteur']
    ordering = ['created']
    inlines = [
        SoumissionArticleInline,
    ]
    list_filter = ('statut',)


admin.site.register(Article, ArticleAdmin)
