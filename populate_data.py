import os
import django
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GPCapital.settings')
django.setup()

from app_gp.models import *
from faker import Faker

# customer_services = models.ManyToManyField('ChoicesCustomerService',
#                                            verbose_name='Atendimentos',
#                                            related_name='client_customer_service_rel',
#                                            db_table='inter_client_customer_services')
#
# places_accepted = models.ManyToManyField('ChoicesPlace',
#                                          verbose_name='Lugares Aceitos',
#                                          db_table='inter_client_places_accepted')
#
# payments_accepted = models.ManyToManyField('ChoicesPaymentAccepted',
#                                            verbose_name='Pagamentos Aceitos',
#                                            db_table='inter_client_payments_accepted')
#
# services_offered = models.ManyToManyField('ChoicesServicesOffered',
#                                           verbose_name='Serviços Oferecidos',
#                                           db_table='inter_client_services_offered')

fake = Faker(locale='pt_BR')

choices_eye_color_ids = list(ChoicesEyeColor.objects.all().values_list('pk', flat=True))
choices_hair_color_ids = list(ChoicesHairColor.objects.all().values_list('pk', flat=True))
choices_ethnicity_ids = list(ChoicesEthnicity.objects.all().values_list('pk', flat=True))
choices_status_ids = list(ChoicesStatus.objects.all().values_list('pk', flat=True))

# Brasília, Santa Maria, Goiânia
choices_cities_ids = [1778, 8087, 2174]

image_profile_list = []
image_profile_dir = 'Media/image_profile_1024_768'
for root, dirs, files in os.walk(image_profile_dir):
    for filename in files:
        image_path = f'{image_profile_dir}/{filename}'
        image_profile_list.append(image_path)

a = 0


def populate(N=10, city_id):
    for instance in range(N):
        name = fake.name_female()
        fake_name = fake.first_name_female()
        short_description = fake.sentence(nb_words=4, variable_nb_words=True, ext_word_list=None)
        description = fake.paragraph(nb_sentences=4, variable_nb_sentences=True, ext_word_list=None)
        image_profile = image_profile_list[instance]
        age = fake.pyint(min_value=18, max_value=40, step=1)
        weight = round(random.uniform(55, 77), 1)
        height = round(random.uniform(1.58, 1.75), 2)
        bust = round(random.uniform(86, 97), 1)
        waist = round(random.uniform(78, 87), 1)
        butt = round(random.uniform(95, 102), 1)
        service_charged = fake.pyint(min_value=150, max_value=450, step=50)

        genre_id = 1
        eye_id = random.choice(choices_eye_color_ids)
        hair_id = random.choice(choices_hair_color_ids)
        ethnicity_id = random.choice(choices_ethnicity_ids)
        status_id = random.choice(choices_status_ids)
        dict_person = {
            'name': name,
            'fake_name': fake_name,
            'short_description': short_description,
            'description': description,
            'image_profile': image_profile,
            'age': age,
            'weight': weight,
            'height': height,
            'bust': bust,
            'waist': waist,
            'butt': butt,
            'service_charged': service_charged,
            'genre_id': genre_id,
            'eye_id': eye_id,
            'hair_id': hair_id,
            'ethnicity_id': ethnicity_id,
            'status_id': status_id
        }
        print(dict_person)

        m = Client(**dict_person)
        m.save()


if __name__ == '__main__':
    for city in choices_cities_ids:
        populate(5, city)
