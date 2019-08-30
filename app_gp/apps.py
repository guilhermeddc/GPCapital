from django.apps import AppConfig


class AppGpConfig(AppConfig):
    name = 'app_gp'

    def ready(self):
        from app_gp.signals import h_choicescity, h_choicesgenre, h_client, h_clientphoto, h_clientvideo, h_highlight


