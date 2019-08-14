import os
import django
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GPCapital.settings')
django.setup()

from app_gp.models import *
from faker import Faker

fake = Faker(locale='pt_BR')

choices_eye_color_ids = list(ChoicesEyeColor.objects.all().values_list('pk', flat=True))
choices_hair_color_ids = list(ChoicesHairColor.objects.all().values_list('pk', flat=True))
choices_ethnicity_ids = list(ChoicesEthnicity.objects.all().values_list('pk', flat=True))
choices_status_ids = list(ChoicesStatus.objects.all().values_list('pk', flat=True))
choices_customer_services_ids = list(ChoicesCustomerService.objects.all().values_list('pk', flat=True))

# Brasília, Santa Maria, Goiânia
choices_cities_ids = [1778, 8087, 2174]

girls_image_profile_list = []
girl_image_profile_dir = 'Media/girls_image_profile_1024_768'
for root, dirs, files in os.walk(girl_image_profile_dir):
    for filename in files:
        image_path = f'{girl_image_profile_dir}/{filename}'
        girls_image_profile_list.append(image_path)

count_girls_image_profile = len(girls_image_profile_list)

men_image_profile_list = []
men_image_profile_dir = 'Media/men_image_profile_1024_768'
for root, dirs, files in os.walk(men_image_profile_dir):
    for filename in files:
        image_path = f'{men_image_profile_dir}/{filename}'
        men_image_profile_list.append(image_path)

count_men_image_profile = len(men_image_profile_list)


def create_client(genre_id=2):
    if genre_id == 1:
        name = fake.name_male()
        fake_name = fake.first_name_male()
        image_profile = men_image_profile_list[fake.random_int(min=0, max=count_men_image_profile)]
    else:
        name = fake.name_female()
        fake_name = fake.first_name_female()
        image_profile = girls_image_profile_list[fake.random_int(min=0, max=count_girls_image_profile)]

    short_description = fake.sentence(nb_words=4, variable_nb_words=True, ext_word_list=None)
    description = fake.paragraph(nb_sentences=4, variable_nb_sentences=True, ext_word_list=None)
    age = fake.pyint(min_value=18, max_value=40, step=1)
    weight = round(random.uniform(55, 77), 1)
    height = round(random.uniform(1.58, 1.75), 2)
    bust = round(random.uniform(86, 97), 1)
    waist = round(random.uniform(78, 87), 1)
    butt = round(random.uniform(95, 102), 1)
    service_charged = fake.pyint(min_value=150, max_value=450, step=50)

    genre_id = genre_id
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

    client = Client(**dict_person)
    client.save()


def create_client_city_sit(client_id, city_id, sit_number):
    dict_client_city_sit = {
        'client_id': client_id,
        'city_id': city_id,
        'sit_number': sit_number,
    }

    client_city_sit = ClientCitySit(**dict_client_city_sit)
    client_city_sit.save()


def create_client_customer_services(client_id, customer_service_id):
    dict_inter_client_customer_services = {
        'client_id': client_id,
        'customer_service_id': customer_service_id,
    }

    inter_client_customer_services = InterClientCustomerServices(**dict_inter_client_customer_services)
    inter_client_customer_services.save()


def create_client_places_accepted(client_id, place_id):
    dict_inter_client_places_accepted = {
        'client_id': client_id,
        'place_id': place_id,
    }

    inter_client_places_accepted = InterClientPlacesAccepted(**dict_inter_client_places_accepted)
    inter_client_places_accepted.save()


def create_client_payments_accepted(client_id, payment_accepted_id):
    dict_inter_client_payments_accepted = {
        'client_id': client_id,
        'payment_accepted_id': payment_accepted_id,
    }

    inter_client_payments_accepted = InterClientPaymentsAccepted(**dict_inter_client_payments_accepted)
    inter_client_payments_accepted.save()


def create_client_services_offered(client_id, services_offered_id):
    dict_inter_client_services_offered = {
        'client_id': client_id,
        'services_offered_id': services_offered_id,
    }

    inter_client_services_offered = InterClientServicesOffered(**dict_inter_client_services_offered)
    inter_client_services_offered.save()


if __name__ == '__main__':
    for city in choices_cities_ids:
        populate(5, city)
