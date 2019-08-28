from PIL import Image
from django.db.models.signals import pre_save, post_delete
from django.utils.text import slugify
from django.core.files.base import ContentFile, BytesIO
from app_gp.utils.utils import unique_slug_generator
from app_gp.models import Client, ChoicesCity, ChoicesGenre
import os

# http://www.lexev.org/en/2016/django-signal-or-model-method/
# 1 - Create submodule signals and place handlers.py in it
# 2 - Define signals in that file handlers.py
# 3 - Create application config class
# 4 - In apps.py overrided ready function to import the handler ex:
#       def ready(self): import app_gp.signals.handlers
# 5 - Add to __init__.py of your app the config class ex:
#       default_app_config = 'app_gp.apps.AppGpConfig'


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
                old_instance.image_profile.delete(save=False)
            if os.path.isfile(old_instance.image_thumb.path):
                old_instance.image_thumb.delete(save=False)
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
        file_name = f'{instance.image_profile.name}'
        instance.image_thumb.save(file_name, ContentFile(thumb_io.getvalue()), save=False)


pre_save.connect(client_pre_save_receiver, sender=Client, dispatch_uid='unique')


def client_post_delete_receiver(sender, instance, **kwargs):
    # Delete Image profile
    if instance.image_profile:
        if os.path.isfile(instance.image_profile.path):
            instance.image_profile.delete(save=False)

    # Delete Thumbnail
    if instance.image_thumb:
        if os.path.isfile(instance.image_thumb.path):
            instance.image_thumb.delete(save=False)


post_delete.connect(client_post_delete_receiver, sender=Client, dispatch_uid='unique')


# CITY
def city_pre_save_receiver(sender, instance, *args, **kwargs):
    # PREVENT FIXTURE ERRORS if (kwargs.get('created', True) and not kwargs.get('raw', False)):
    if not kwargs.get('raw', False):
        # IF PK EXIST SO WE ARE SAVING FOR CHANGE SOME FIELD
        # ELSE WE ARE CREATING THE DATA FOR THE FIRST TIME
        a = kwargs.get('created')
        if instance.pk:

            try:
                # GET Instance before change anything
                old_instance = sender.objects.get(pk=instance.pk)
            except sender.DoesNotExist:
                return

            # City name or State changed? IF yes, recreate the slug field
            if not ((old_instance.city == instance.city) or (old_instance.state == instance.state)):
                slug_candidate = f'{instance.city}-{instance.state}'
                slug = slugify(slug_candidate)
                instance.slug = unique_slug_generator(instance=instance, slug=slug)

        else:   # FIRST TIME
            # Create slug
            slug_candidate = f'{instance.city}-{instance.state}'
            slug = slugify(slug_candidate)
            instance.slug = unique_slug_generator(instance=instance, slug=slug)


pre_save.connect(city_pre_save_receiver, sender=ChoicesCity, dispatch_uid='unique')


# GENRE
def genre_pre_save_receiver(sender, instance, *args, **kwargs):
    # PREVENT FIXTURE ERRORS if (kwargs.get('created', True) and not kwargs.get('raw', False)):
    if not kwargs.get('raw', False):
        # IF PK EXIST SO WE ARE SAVING FOR CHANGE SOME FIELD
        # ELSE WE ARE CREATING THE DATA FOR THE FIRST TIME
        if instance.pk:
            # GET Instance before change anything
            old_instance = sender.objects.get(pk=instance.pk)

            # Genre site name changed? IF yes, recreate the slug field
            if not old_instance.site_name == instance.site_name:
                slug_candidate = f'{instance.site_name}'
                slug = slugify(slug_candidate)
                instance.slug = unique_slug_generator(instance=instance, slug=slug)

        else:   # FIRST TIME
            # Create slug
            slug_candidate = f'{instance.site_name}'
            slug = slugify(slug_candidate)
            instance.slug = unique_slug_generator(instance=instance, slug=slug)


pre_save.connect(genre_pre_save_receiver, sender=ChoicesGenre, dispatch_uid='unique')
