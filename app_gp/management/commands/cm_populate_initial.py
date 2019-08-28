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
        for obj in hair_color:
            ChoicesHairColor.objects.create(hair_color=obj)

        ChoicesLanguage.objects.all().delete()
        choices_languages = ["Português", "Inglês", "Espanhol", "Alemão"]
        for obj in choices_languages:
            ChoicesLanguage.objects.create(choices_languages=obj)

        ChoicesPaymentAccepted.objects.all().delete()
        choices_payment_accepted = ["Cartão de crédito", "Cartão de débito", "Dinheiro"]
        for obj in choices_payment_accepted:
            ChoicesPaymentAccepted.objects.create(choices_payment_accepted=obj)

        ChoicesPlace.objects.all().delete()
        choices_place = ["Local próprio", "Hotéis / Motéis / Domicílio", "Eventos", "Viagens"]
        for obj in choices_place:
            ChoicesPlace.objects.create(choices_place=obj)

        self.stdout.write(self.style.SUCCESS('INSERTED!'))
