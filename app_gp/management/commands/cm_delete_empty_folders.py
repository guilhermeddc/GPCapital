import os

from django.core.management.base import BaseCommand
from django.conf import settings


class Command(BaseCommand):
    def handle(self, *args, **options):

        media_root = getattr(settings, 'MEDIA_ROOT', None)

        # Bottom-up - delete all empty folders
        for relative_root, dirs, files in os.walk(media_root, topdown=False):
            for dir_ in dirs:
                if not os.listdir(os.path.join(relative_root, dir_)):
                    os.rmdir(os.path.join(relative_root, dir_))
