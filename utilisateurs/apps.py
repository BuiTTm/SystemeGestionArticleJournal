from django.apps import AppConfig


class UtilisateurConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'utilisateurs'

    # def ready(self):
    #     from . import signals