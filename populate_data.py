import os

import django

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
choices_place_ids = list(ChoicesPlace.objects.all().values_list('pk', flat=True))
choices_payment_accepted_ids = list(ChoicesPaymentAccepted.objects.all().values_list('pk', flat=True))
choices_services_offered_ids = list(ChoicesServicesOffered.objects.all().values_list('pk', flat=True))

# Brasília, Santa Maria, Goiânia, Belo Horizonte, São Paulo
choices_cities_ids = [1778, 8087, 2174, 2754, 9668]

girls_image_profile_list = []
girl_image_profile_dir = 'Media/girls_image_profile_1024_768'
for root, dirs, files in os.walk(girl_image_profile_dir):
    for filename in files:
        image_path = f'{girl_image_profile_dir}/{filename}'
        girls_image_profile_list.append(image_path)

count_girls_image_profile = len(girls_image_profile_list) - 1

men_image_profile_list = []
men_image_profile_dir = 'Media/men_image_profile_1024_768'
for root, dirs, files in os.walk(men_image_profile_dir):
    for filename in files:
        image_path = f'{men_image_profile_dir}/{filename}'
        men_image_profile_list.append(image_path)

count_men_image_profile = len(men_image_profile_list) - 1


def create_client(
        genre_id=None,
        eye_id=None,
        hair_id=None,
        ethnicity_id=None,
        status_id=None):

    if genre_id is None:
        genre_id = random.randint(1, 2)

    if eye_id is None:
        eye_id = random.choice(choices_eye_color_ids)

    if hair_id is None:
        hair_id = random.choice(choices_hair_color_ids)

    if ethnicity_id is None:
        ethnicity_id = random.choice(choices_ethnicity_ids)

    if status_id is None:
        status_id = random.choice(choices_status_ids)

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

    return client


def create_client_city_sit(client_id, city_id, sit_number):
    dict_client_city_sit = {
        'client_id': client_id,
        'city_id': city_id,
        'sit_number': sit_number,
    }

    client_city_sit = ClientCitySit(**dict_client_city_sit)
    client_city_sit.save()


def create_client_customer_services(client_id):

    len_choice = len(choices_customer_services_ids)
    r_number = random.randint(1, len_choice)
    samples = random.sample(choices_customer_services_ids, r_number)

    for i in samples:

        dict_inter_client_customer_services = {
            'client_id': client_id,
            'customer_service_id': i,
        }

        inter_client_customer_services = InterClientCustomerServices(**dict_inter_client_customer_services)
        inter_client_customer_services.save()


def create_client_places_accepted(client_id):
    len_choice = len(choices_place_ids)
    r_number = random.randint(1, len_choice)
    samples = random.sample(choices_place_ids, r_number)

    for i in samples:
        dict_inter_client_places_accepted = {
            'client_id': client_id,
            'place_id': i,
        }

        inter_client_places_accepted = InterClientPlacesAccepted(**dict_inter_client_places_accepted)
        inter_client_places_accepted.save()


def create_client_payments_accepted(client_id):
    len_choice = len(choices_payment_accepted_ids)
    r_number = random.randint(1, len_choice)
    samples = random.sample(choices_payment_accepted_ids, r_number)

    for i in samples:
        dict_inter_client_payments_accepted = {
            'client_id': client_id,
            'payment_accepted_id': i,
        }

        inter_client_payments_accepted = InterClientPaymentsAccepted(**dict_inter_client_payments_accepted)
        inter_client_payments_accepted.save()


def create_client_services_offered(client_id):
    len_choice = len(choices_services_offered_ids)
    r_number = random.randint(1, len_choice)
    samples = random.sample(choices_services_offered_ids, r_number)

    for i in samples:
        dict_inter_client_services_offered = {
            'client_id': client_id,
            'services_offered_id': i,
        }

        inter_client_services_offered = InterClientServicesOffered(**dict_inter_client_services_offered)
        inter_client_services_offered.save()


if __name__ == '__main__':

    active_girls = 10
    active_men = 5

    for city_id in choices_cities_ids:

        last_id_sit = ClientCitySit.objects.filter(city_id=city_id).order_by('-sit_number')[0].sit_number

        for i in range(1, active_girls+1):
            girl = create_client(status_id=1, genre_id=2)

            id_sit = last_id_sit + i
            create_client_city_sit(client_id=girl.id, city_id=city_id, sit_number=id_sit)

            create_client_customer_services(client_id=girl.id)
            create_client_places_accepted(client_id=girl.id)
            create_client_payments_accepted(client_id=girl.id)
            create_client_services_offered(client_id=girl.id)

        men_start = active_girls + 1
        men_end = active_girls + active_men + 1
        last_id_sit = ClientCitySit.objects.filter(city_id=city_id).order_by('-sit_number')[0].sit_number
        for i in range(men_start, men_end):
            men = create_client(status_id=1, genre_id=1)

            id_sit = last_id_sit + i
            create_client_city_sit(client_id=men.id, city_id=city_id, sit_number=id_sit)

            create_client_customer_services(client_id=men.id)
            create_client_places_accepted(client_id=men.id)
            create_client_payments_accepted(client_id=men.id)
            create_client_services_offered(client_id=men.id)
