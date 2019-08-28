from django.core.management.base import BaseCommand
from app_gp.models import *


class Command(BaseCommand):

    def handle(self, *args, **options):

        customer_service = ["Casais", "Mulheres", "Homens", "Deficiente física"]
        for obj in customer_service:
            ChoicesCustomerService.objects.create(customer_service=obj)

        ethnicity = ["Branco", "Mestiço", "Mulato", "Negro", "Oriental", "Pardo"]
        for obj in ethnicity:
            ChoicesEthnicity.objects.create(ethnicity=obj)

        self.stdout.write(self.style.SUCCESS('INSERTED!'))
