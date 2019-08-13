from django.utils.text import slugify


def unique_slug_generator(instance, counter=0):

    slug = slugify(instance.fake_name)

    if counter > 0:
        slug = "{slug}-{number}".format(slug=slug, number=counter)

    klass = instance.__class__

    qs_exists = klass.objects.filter(slug=slug).exclude(id=instance.id).exists()

    if qs_exists:
        return unique_slug_generator(instance, counter=counter+1)

    return slug
