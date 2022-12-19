from django.db.models.signals import post_save
from django.apps import AppConfig
from .signals import create_comite
from .models import Comite


class JournalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'soumissionArticle'

    def ready(self):
        post_save.connect(create_comite, sender=Comite)
