from django.apps import AppConfig


class NanostroiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'nanostroi'

    def ready(self):
        import nanostroi.signals
