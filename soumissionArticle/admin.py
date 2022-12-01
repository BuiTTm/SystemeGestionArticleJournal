from django.contrib import admin
from .models import ArticleSubmission

class JournalAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

admin.site.register(ArticleSubmission, JournalAdmin)
