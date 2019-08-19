from PIL import Image
from django.utils.text import slugify
from django.dispatch import receiver
from django.core.files.base import ContentFile, BytesIO
from django.db import models
from app_gp.utils.utils import unique_slug_generator
from app_gp.models import Client
import os

# http://www.lexev.org/en/2016/django-signal-or-model-method/
# 1 - Create submodule signals and place handlers.py in it
# 2 - Define signals in that file handlers.py
# 3 - Create application config class
# 4 - In apps.py overrided ready function to import the handler ex:
#       def ready(self): import app_gp.signals.handlers
# 5 - Add to __init__.py of your app the config class ex:
#       default_app_config = 'app_gp.apps.AppGpConfig'


@receiver(models.signals.pre_save, sender=Client)
def client_pre_save_receiver(sender, instance, *args, **kwargs):

    # IF PK EXIST SO WE ARE SAVING FOR CHANGE SOME FIELD
    # ELSE WE ARE CREATING THE DATA FOR THE FIRST TIME
    if instance.pk:
        # GET Instance before change anything
        old_instance = sender.objects.get(pk=instance.pk)

        # Fake name changed? IF yes, recreate the slug field
        if not old_instance.fake_name == instance.fake_name:
            slug = slugify(instance.fake_name)
            instance.slug = unique_slug_generator(instance=instance, slug=slug)

        # Image profile changed? IF yes, delete old image and old thumb from path
        if not old_instance.image_profile == instance.image_profile:
            if os.path.isfile(old_instance.image_profile.path):
                os.remove(old_instance.image_profile.path)
            if os.path.isfile(old_instance.image_thumb.path):
                os.remove(old_instance.image_thumb.path)
            create_thumb = True
        else:
            create_thumb = False

    else:   # FIRST TIME
        # Create slug
        slug = slugify(instance.fake_name)
        instance.slug = unique_slug_generator(instance=instance, slug=slug)
        create_thumb = True

    # THIS CODE WIL RUN IN EVERY SAVE
    if create_thumb:
        # Create thumbnail from profile image
        img = Image.open(instance.image_profile)

        # Change image to thumbnail with specific size and save in a BytesIO
        img.thumbnail((300, 300), Image.ANTIALIAS)
        thumb_io = BytesIO()
        img.save(thumb_io, img.format, quality=100)

        # Create the filename and save the thumb image to thumb field
        file_name = f'{os.path.splitext(instance.image_profile.name)[0]}_thumb.jpg'
        instance.image_thumb.save(file_name, ContentFile(thumb_io.getvalue()), save=False)


@receiver(models.signals.post_delete, sender=Client)
def client_post_delete_receiver(sender, instance, **kwargs):
    # Delete Image profile
    if instance.image_profile:
        if os.path.isfile(instance.image_profile.path):
            os.remove(instance.image_profile.path)

    # Delete Thumbnail
    if instance.image_thumb:
        if os.path.isfile(instance.image_thumb.path):
            os.remove(instance.image_thumb.path)
