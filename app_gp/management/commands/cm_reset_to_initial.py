from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Deleting all data and insert initial...'))
        call_command('cm_populate_initial')
        self.stdout.write(self.style.SUCCESS('Deleting empty folders...'))
        call_command('cm_delete_empty_folders')
        self.stdout.write(self.style.SUCCESS('Creating Super User...'))
        call_command('cm_create_super_user')
        self.stdout.write(self.style.SUCCESS('Populating fake data...'))
        call_command('cm_fake_populate')

