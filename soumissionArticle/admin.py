from django.contrib import admin
from .models import SoumissionArticle, Article, Comite, Commentaire


class SoumissionArticleInline(admin.StackedInline):
    model = SoumissionArticle
    readonly_fields = ['lien']
    extra = 0


class ComiteInline(admin.StackedInline):
    model = Comite
    extra = 0
    can_delete = False
    list_display = ['id']

    def has_add_permission(self, req, obj=None):
        if obj and obj.statut == Article.Statut.EN_ATTENTE:
            return True
        else:
            return False


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['titre', 'statut', 'auteur']
    ordering = ['created']
    inlines = [
        SoumissionArticleInline,
        ComiteInline
    ]
    list_filter = ('statut',)


class ComiteAdmin(admin.ModelAdmin):
    list_display = ['article', 'date_limite_evaluation']

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['article']
        else:
            return []

    def save_model(self, request, obj, form, change):
        article = Article.objects.get(id=obj.article_id)
        if article.statut == Article.Statut.EN_ATTENTE:
            article.statut = Article.Statut.RELECTURE
            article.save()
        super().save_model(request, obj, form, change)


class CommentaireAdmin(admin.ModelAdmin):
    list_display = ['text', 'evaluateur', 'comite', 'soumission']
    ordering = ['created']


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comite, ComiteAdmin)
admin.site.register(Commentaire, CommentaireAdmin)
