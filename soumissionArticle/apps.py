from django.db.models.signals import post_save
from django.apps import AppConfig


class JournalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'soumissionArticle'

    def ready(self):
        from .models import Comite
        from .signals import create_comite
        post_save.connect(create_comite, sender=Comite)
