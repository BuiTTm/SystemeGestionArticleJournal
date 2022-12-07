from django.apps import AppConfig


class UtilisateurConfig(AppConfig):
    name = 'profiles'
    verbose_name = 'User Profiles'

    def ready(self):
        from . import signals