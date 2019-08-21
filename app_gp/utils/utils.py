from django.utils.text import slugify
from PIL import Image
import os


def unique_slug_generator(instance, slug='', counter=0):

    if counter > 0:
        slug = "{number}-{slug}".format(slug=slug, number=counter)

    klass = instance.__class__

    qs_exists = klass.objects.filter(slug=slug).exclude(id=instance.id).exists()

    if qs_exists:
        return unique_slug_generator(instance, slug=slug, counter=counter + 1)

    return slug


def images_resize_path(from_path='',
                       to_path='',
                       square_fit_size=300,
                       prefix_name='image',
                       save_as_jpg=True):
    if save_as_jpg:
        ext = 'jpg'
    else:
        ext = 'png'

    image_number = 1
    for root, dirs, files in os.walk(from_path):
        for filename in files:
            if filename.endswith('.png') or filename.endswith('.jpg'):
                filename = os.path.join(root, filename)
                im = Image.open(filename)
                width, height = im.size

                if width > height:
                    height = int((square_fit_size / width) * height)
                    width = square_fit_size
                else:
                    width = int((square_fit_size / height) * width)
                    height = square_fit_size

                # Redimensiona a imagem
                im = im.resize((width, height))

                save_path_name = os.path.join(to_path, f'{prefix_name}_{image_number}.{ext}')
                image_number = image_number + 1

                im.save(save_path_name)


def image_resize(image=Image,
                 square_fit_size=300,
                 prefix_name='image',
                 postfix_name='thumb',
                 save_as_jpg=True):
    a = 0
    if save_as_jpg:
        ext = 'jpg'
    else:
        ext = 'png'

    im = Image.open(image)
    width, height = im.size

    if width > height:
        height = int((square_fit_size / width) * height)
        width = square_fit_size
    else:
        width = int((square_fit_size / height) * width)
        height = square_fit_size

    # Redimensiona a imagem
    im = im.resize((width, height))

    save_path_name = os.path.join(to_path, f'{prefix_name}_{postfix_name}.{ext}')

    im.save(save_path_name)
