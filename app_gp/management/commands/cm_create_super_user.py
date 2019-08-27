from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    
    def handle(self, *args, **options):
        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser("admin", "admin@gmail.com", "admin")
            self.stdout.write(self.style.SUCCESS('Successfully created new super user'))
        else:
            self.stdout.write(self.style.SUCCESS('User Admin already exist!'))
