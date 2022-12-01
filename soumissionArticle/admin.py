from django.contrib import admin
from .models import SoumissionArticle

class JournalAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

admin.site.register(SoumissionArticle, JournalAdmin)
