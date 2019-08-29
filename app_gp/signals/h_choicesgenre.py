from django.db.models.signals import pre_save, post_delete
from app_gp.models import ChoicesGenre
from django.utils.text import slugify
from app_gp.utils.utils import unique_slug_generator


def choices_genre_pre_save_receiver(sender, instance, *args, **kwargs):
    # PREVENT FIXTURE ERRORS if (kwargs.get('created', True) and not kwargs.get('raw', False)):
    if not kwargs.get('raw', False):
        # IF PK EXIST SO WE ARE SAVING FOR CHANGE SOME FIELD
        # ELSE WE ARE CREATING THE DATA FOR THE FIRST TIME
        if instance.pk:
            # GET Instance before change anything
            old_instance = sender.objects.get(pk=instance.pk)

            # Genre site name changed? IF yes, recreate the slug field
            if not old_instance.site_name == instance.site_name:
                instance.slug = create_city_slug(instance)

        else:   # FIRST TIME
            # Create slug
            instance.slug = create_city_slug(instance)


pre_save.connect(choices_genre_pre_save_receiver, sender=ChoicesGenre, dispatch_uid='choices_genre_pre_save')


def create_city_slug(instance):
    slug_candidate = f'{instance.site_name}'
    slug = slugify(slug_candidate)
    return unique_slug_generator(instance=instance, slug=slug)
