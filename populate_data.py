import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GPCapital.settings.local')
django.setup()

from app_gp.models import *
from faker import Faker
from django.db.models import Q

fake = Faker(locale='pt_BR')

choices_eye_color_ids = list(ChoicesEyeColor.objects.all().values_list('pk', flat=True))
choices_hair_color_ids = list(ChoicesHairColor.objects.all().values_list('pk', flat=True))
choices_ethnicity_ids = list(ChoicesEthnicity.objects.all().values_list('pk', flat=True))
choices_status_ids = list(ChoicesStatus.objects.all().values_list('pk', flat=True))
choices_languages_ids = list(ChoicesLanguage.objects.all().values_list('pk', flat=True))

choices_customer_services_ids = list(ChoicesCustomerService.objects.all().values_list('pk', flat=True))
choices_place_ids = list(ChoicesPlace.objects.all().values_list('pk', flat=True))
choices_payment_accepted_ids = list(ChoicesPaymentAccepted.objects.all().values_list('pk', flat=True))
choices_services_offered_ids = list(ChoicesServicesOffered.objects.all().values_list('pk', flat=True))

# Brasília, Santa Maria, Goiânia, Belo Horizonte, São Paulo
choices_cities_ids = [1761, 7989, 2133, 2709, 9560]

# GIRLS
girls_image_profile_list = []
girl_image_profile_dir = 'Media/girls_image_profile_1024_768'
for root, dirs, files in os.walk(girl_image_profile_dir):
    for filename in files:
        image_path = f'{girl_image_profile_dir}/{filename}'
        girls_image_profile_list.append(image_path)

count_girls_image_profile = len(girls_image_profile_list) - 1

girls_photos_list = []
girls_photos_profile_dir = 'Media/girls_images_shuffle_size'
for root, dirs, files in os.walk(girls_photos_profile_dir):
    for filename in files:
        image_path = f'{girls_photos_profile_dir}/{filename}'
        girls_photos_list.append(image_path)

count_girls_photos = len(girls_photos_list) - 1

girls_videos_list = []
girls_videos_profile_dir = 'Media/girls_videos'
for root, dirs, files in os.walk(girls_videos_profile_dir):
    for filename in files:
        image_path = f'{girls_videos_profile_dir}/{filename}'
        girls_videos_list.append(image_path)

count_girls_videos = len(girls_videos_list) - 1

# MEN
men_image_profile_list = []
men_image_profile_dir = 'Media/men_image_profile_1024_768'
for root, dirs, files in os.walk(men_image_profile_dir):
    for filename in files:
        image_path = f'{men_image_profile_dir}/{filename}'
        men_image_profile_list.append(image_path)

count_men_image_profile = len(men_image_profile_list) - 1

men_photos_list = []
men_photos_profile_dir = 'Media/men_images_shuffle_size'
for root, dirs, files in os.walk(men_photos_profile_dir):
    for filename in files:
        image_path = f'{men_photos_profile_dir}/{filename}'
        men_photos_list.append(image_path)

count_men_photos = len(men_photos_list) - 1

men_videos_list = []
men_videos_profile_dir = 'Media/men_videos'
for root, dirs, files in os.walk(men_videos_profile_dir):
    for filename in files:
        image_path = f'{men_videos_profile_dir}/{filename}'
        men_videos_list.append(image_path)

count_men_videos = len(men_videos_list) - 1


def create_client(
        genre_id=None,
        eye_id=None,
        hair_id=None,
        ethnicity_id=None,
        status_id=None,
        profile_priority=None,
        city_id=None):
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

    contact_email = fake.ascii_safe_email()
    short_description = fake.sentence(nb_words=4, variable_nb_words=True, ext_word_list=None)
    description = fake.paragraph(nb_sentences=4, variable_nb_sentences=True, ext_word_list=None)
    phone = fake.msisdn()
    age = fake.pyint(min_value=18, max_value=40, step=1)
    weight = round(random.uniform(55, 77), 1)
    height = round(random.uniform(1.58, 1.75), 2)
    bust = round(random.uniform(86, 97), 1)
    waist = round(random.uniform(78, 87), 1)
    hip = round(random.uniform(80, 90), 1)
    butt = round(random.uniform(95, 102), 1)
    foot = round(random.uniform(35, 39), 1)
    service_charged = fake.pyint(min_value=150, max_value=450, step=50)

    dict_person = {
        'name': name,
        'fake_name': fake_name,
        'contact_email': contact_email,
        'short_description': short_description,
        'description': description,
        'phone': phone,
        'image_profile': image_profile,
        'profile_priority': profile_priority,
        'city_id': city_id,
        'age': age,
        'weight': weight,
        'height': height,
        'bust': bust,
        'waist': waist,
        'hip': hip,
        'butt': butt,
        'service_charged': service_charged,
        'foot': foot,
        'genre_id': genre_id,
        'eye_id': eye_id,
        'hair_id': hair_id,
        'ethnicity_id': ethnicity_id,
        'status_id': status_id
    }

    client = Client(**dict_person)
    client.save()

    return client


def create_client_languages(client_id):
    len_choice = len(choices_languages_ids)
    r_number = random.randint(1, len_choice)
    samples = random.sample(choices_languages_ids, r_number)

    for i in samples:
        dict_inter_client_language = {
            'client_id': client_id,
            'language_id': i,
        }

        inter_client_language = InterClientLanguages(**dict_inter_client_language)
        inter_client_language.save()


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


def create_client_photo(client_id, genre_id, n_samples=5):
    for n in range(n_samples):
        if genre_id == 1:
            photo = men_photos_list[fake.random_int(min=0, max=count_men_photos)]
        else:
            photo = girls_photos_list[fake.random_int(min=0, max=count_girls_photos)]

        dict_client_photo = {
            'client_id': client_id,
            'photo': photo,
            'order_priority': n,
        }

        client_photo = ClientPhoto(**dict_client_photo)
        client_photo.save()


def create_client_video(client_id, genre_id, n_samples=5):
    for n in range(n_samples):
        if genre_id == 1:
            video = men_videos_list[fake.random_int(min=0, max=count_men_videos)]
        else:
            video = girls_videos_list[fake.random_int(min=0, max=count_girls_videos)]

        dict_client_video = {
            'client_id': client_id,
            'video': video,
            'order_priority': n,
        }

        client_video = ClientVideo(**dict_client_video)
        client_video.save()


if __name__ == '__main__':

    # for city in ChoicesCity.objects.all():
    #     uf_name = city.state
    #     state_id = ChoicesStates.objects.filter(uf=uf_name)[0].id
    #     city.uf_id = state_id
    #     city.save()
    active_men = 5
    active_girls = 10
    genre_list = [active_men, active_girls]

    genre_id = 0
    for genre_number in genre_list:
        genre_id = genre_id + 1

        for city_id in choices_cities_ids:
            priority = 1
            last_number = Client.objects.filter(city_id=city_id, genre_id=genre_id).order_by('-profile_priority')
            if last_number:
                priority = last_number[0].profile_priority

            for i in range(1, genre_number + 1):
                priority = priority + i

                person = create_client(status_id=1, genre_id=genre_id, city_id=city_id, profile_priority=priority)

                create_client_languages(client_id=person.id)
                create_client_customer_services(client_id=person.id)
                create_client_places_accepted(client_id=person.id)
                create_client_payments_accepted(client_id=person.id)
                create_client_services_offered(client_id=person.id)

                n_samples = random.randint(3, 10)
                create_client_photo(client_id=person.id, genre_id=genre_id, n_samples=n_samples)

                n_samples = random.randint(1, 5)
                create_client_video(client_id=person.id, genre_id=genre_id, n_samples=n_samples)
