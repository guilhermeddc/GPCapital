from django.core.management.base import BaseCommand
from app_gp.models import *


class Command(BaseCommand):

    def handle(self, *args, **options):

        ChoicesCustomerService.objects.all().delete()
        customer_service = ["Casais", "Mulheres", "Homens", "Deficiente física"]
        for obj in customer_service:
            ChoicesCustomerService.objects.create(customer_service=obj)

        ChoicesEthnicity.objects.all().delete()
        ethnicity = ["Branco", "Mestiço", "Mulato", "Negro", "Oriental", "Pardo"]
        for obj in ethnicity:
            ChoicesEthnicity.objects.create(ethnicity=obj)

        ChoicesEyeColor.objects.all().delete()
        eye_color = ["Azuis", "Castanhos", "Verdes", "Outras cores"]
        for obj in eye_color:
            ChoicesEyeColor.objects.create(eye_color=obj)

        # ChoicesGenre.objects.all().delete()
        # eye_color = ["Azuis", "Castanhos", "Verdes", "Outras cores"]
        # for obj in eye_color:
        #     ChoicesGenre.objects.create(eye_color=obj)

        ChoicesHairColor.objects.all().delete()
        hair_color = ["Loiros", "Ruivos", "Castanhos", "Pretos", "Grisalhos", "Outras cores"]
        for obj in eye_color:
            ChoicesHairColor.objects.create(hair_color=obj)

        self.stdout.write(self.style.SUCCESS('INSERTED!'))
