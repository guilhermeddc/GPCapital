from django.db.models.signals import pre_save, post_delete
from app_gp.models import ClientPhoto


# http://www.lexev.org/en/2016/django-signal-or-model-method/
# 1 - Create submodule signals and place handlers.py in it
# 2 - Define signals in that file handlers.py
# 3 - Create application config class
# 4 - In apps.py overrided ready function to import the handler ex:
#       def ready(self): import app_gp.signals.handlers
# 5 - Add to __init__.py of your app the config class ex:
#       default_app_config = 'app_gp.apps.AppGpConfig'


def client_photo_pre_save_receiver(sender, instance, *args, **kwargs):

    # IF PK EXIST SO WE ARE SAVING FOR CHANGE SOME FIELD
    # ELSE WE ARE CREATING THE DATA FOR THE FIRST TIME
    if instance.pk:
        # GET Instance before change anything
        old_instance = sender.objects.get(pk=instance.pk)

        # Photo changed? Delete old one
        if not old_instance.photo == instance.photo:
            if old_instance.photo:
                old_instance.photo.delete(save=False)


pre_save.connect(client_photo_pre_save_receiver, sender=ClientPhoto, dispatch_uid='client_photo_pre_save')


def client_photo_post_delete_receiver(sender, instance, **kwargs):
    # Delete Image photo
    if instance.photo:
        instance.photo.delete(save=False)


post_delete.connect(client_photo_post_delete_receiver, sender=ClientPhoto, dispatch_uid='client_photo_post_delete')
