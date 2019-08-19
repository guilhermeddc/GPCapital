from django.apps import AppConfig


class AppGpConfig(AppConfig):
    name = 'app_gp'

    def ready(self):
        from app_gp.signals import handlers

