from django.apps import AppConfig


class AppGpConfig(AppConfig):
    name = 'app_gp'

    def ready(self):
        import app_gp.signals.handlers
