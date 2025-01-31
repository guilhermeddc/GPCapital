import random
from django.db import models
import os


class ChoicesQuestion(models.Model):
    question = models.CharField('Pergunta', max_length=255, null=False, blank=False)

    class Meta:
        verbose_name = 'Pergunta'
        verbose_name_plural = 'Perguntas'
        ordering = ['question']
        db_table = 'choices_question'

    def __str__(self):
        return self.question


class ChoicesEthnicity(models.Model):
    ethnicity = models.CharField('Etnia', max_length=50, null=False, blank=False)

    class Meta:
        verbose_name = 'Etnia'
        verbose_name_plural = 'Etnias'
        ordering = ['ethnicity']
        db_table = 'choices_ethnicity'

    def __str__(self):
        return self.ethnicity


class GenresQuerySet(models.QuerySet):

    def get_genres_by_city(self, slug):
        city_id = ChoicesCity.objects.filter(slug=slug).first().id
        select = "SELECT DISTINCT genre.id, genre.slug, genre.genre, genre.site_name, genre.representative_image " \
                 "FROM choices_genre AS genre " \
                 "INNER JOIN client ON genre.id = client.genre_id " \
                 "WHERE client.city_id = %s " \
                 "ORDER BY genre.id"
        return self.raw(select, params=[city_id])


class GenreManager(models.Manager):
    def get_queryset(self):
        return GenresQuerySet(self.model, using=self._db)

    def get_genres_by_city(self, slug):
        return self.get_queryset().get_genres_by_city(slug)


class ChoicesGenre(models.Model):
    objects = GenreManager()

    slug = models.SlugField('slug', max_length=50, blank=True, unique=True)
    genre = models.CharField('Gênero', max_length=50, null=False, blank=False)
    site_name = models.CharField('Nome no site', max_length=50, null=False, blank=False)
    representative_image = models.ImageField('Imagem representativa', upload_to='genero_images', null=True, blank=True)

    class Meta:
        verbose_name = 'Gênero'
        verbose_name_plural = 'Gêneros'
        ordering = ['genre']
        db_table = 'choices_genre'

    def __str__(self):
        return self.genre


class ChoicesEyeColor(models.Model):
    eye_color = models.CharField('Cor do olho', max_length=75, null=False, blank=False)

    class Meta:
        verbose_name = 'Cor do olho'
        verbose_name_plural = 'Cores dos olhos'
        ordering = ['eye_color']
        db_table = 'choices_eye_color'

    def __str__(self):
        return self.eye_color


class ChoicesHairColor(models.Model):
    hair_color = models.CharField('Cor do cabelo', max_length=50, null=False, blank=False)

    class Meta:
        verbose_name = 'Cor de cabelo'
        verbose_name_plural = 'Cores de cabelo'
        ordering = ['hair_color']
        db_table = 'choices_hair_color'

    def __str__(self):
        return self.hair_color


class ChoicesCustomerService(models.Model):
    customer_service = models.CharField('Tipos de atendimento', max_length=50, null=False, blank=False)

    class Meta:
        verbose_name = 'Atendimento'
        verbose_name_plural = 'Atendimentos'
        ordering = ['customer_service']
        db_table = 'choices_customer_service'

    def __str__(self):
        return self.customer_service


class ChoicesPlace(models.Model):
    place = models.CharField('Lugares', max_length=50, null=False, blank=False)

    class Meta:
        verbose_name = 'Lugar'
        verbose_name_plural = 'Lugares'
        ordering = ['place']
        db_table = 'choices_place'

    def __str__(self):
        return self.place


class ChoicesPaymentAccepted(models.Model):
    payment = models.CharField('Pagamento', max_length=50, null=False, blank=False)

    class Meta:
        verbose_name = 'Pagamento'
        verbose_name_plural = 'Pagamentos'
        ordering = ['payment']
        db_table = 'choices_payment_accepted'

    def __str__(self):
        return self.payment


class ChoicesServicesOffered(models.Model):
    services = models.CharField('Serviços', max_length=50, null=False, blank=False)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'
        ordering = ['services']
        db_table = 'choices_services_offered'

    def __str__(self):
        return self.services


class ChoicesStates(models.Model):
    uf = models.CharField('UF', max_length=5, null=False)
    state = models.CharField('Estado', max_length=75, null=False)
    ibge_code = models.IntegerField('Código IBGE', null=False)

    class Meta:
        verbose_name = 'UF'
        verbose_name_plural = 'UF'
        ordering = ['uf']
        db_table = 'choices_states'

    def __str__(self):
        return self.uf


class CitiesQuerySet(models.QuerySet):

    def worked_cities(self):
        existing_city_ids = Client.objects.values('city_id').distinct().order_by('city_id')
        return ChoicesCity.objects.filter(id__in=existing_city_ids)


class CityManager(models.Manager):
    def get_queryset(self):
        return CitiesQuerySet(self.model, using=self._db)

    def worked_cities(self):
        return self.get_queryset().worked_cities()


class ChoicesCity(models.Model):
    objects = CityManager()

    slug = models.SlugField('slug', max_length=255, unique=True)
    state = models.ForeignKey('ChoicesStates', verbose_name='Estado', on_delete=models.DO_NOTHING, null=False)
    city = models.CharField('Cidade', max_length=255, null=False)
    cep = models.CharField('Cep', max_length=10, null=True)
    ibge_code = models.CharField('Código IBGE', max_length=255, null=False)
    area = models.FloatField('Area', null=True)
    subordinate_municipality = models.IntegerField('Município subordinado', null=False)

    class Meta:
        verbose_name = 'Cidade'
        verbose_name_plural = 'Cidades'
        ordering = ['city']
        db_table = 'choices_city'

    def __str__(self):
        return f'{self.city}'


class ChoicesNeighborhoods(models.Model):
    neighborhood = models.CharField('Bairro', max_length=255, null=False)
    city = models.ForeignKey('ChoicesCity', verbose_name='Cidade', on_delete=models.DO_NOTHING, null=False)

    class Meta:
        verbose_name = 'Bairro'
        verbose_name_plural = 'Bairros'
        ordering = ['city', 'neighborhood']
        db_table = 'choices_neighborhoods'

    def __str__(self):
        return self.neighborhood


class ChoicesLanguage(models.Model):
    language = models.CharField('Idioma', max_length=50, null=False)

    class Meta:
        verbose_name = 'Idioma'
        verbose_name_plural = 'Idiomas'
        ordering = ['language']
        db_table = 'choices_language'

    def __str__(self):
        return self.language


def profile_upload_path(instance, filename):
    # basic_path = get_basic_path(instance)
    base_name = os.path.basename(filename)
    # path = f'{basic_path}/profile/{base_name}'
    path = f'{instance.genre.slug}/{instance.slug}/profile/{base_name}'
    return path


def thumb_upload_path(instance, filename):
    # basic_path = get_basic_path(instance)
    base_name = os.path.basename(filename)
    name, ext = os.path.splitext(base_name)
    # Rename to filename_thumb.jpg
    new_name = f'{name}_thumb{ext}'
    # path = f'{basic_path}/profile/{new_name}'
    path = f'{instance.genre.slug}/{instance.slug}/profile/{new_name}'
    return path


def highlight_photo_upload_path(instance, filename):
    base_name = os.path.basename(filename)
    path = f'destaques/{instance.city.slug}/{instance.genre.slug}/{instance.get_highlight_type_display()}/{base_name}'
    return path


def photos_upload_path(instance, filename):
    base_name = os.path.basename(filename)
    path = f'{instance.client.genre.slug}/{instance.client.slug}/photos/{base_name}'
    return path


def videos_upload_path(instance, filename):
    base_name = os.path.basename(filename)
    path = f'{instance.client.genre.slug}/{instance.client.slug}/videos/{base_name}'
    return path


class ChoicesStatus(models.Model):
    status = models.CharField('Status', max_length=50, unique=True)

    def __str__(self):
        return self.status

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Status'
        ordering = ['status']
        db_table = 'choices_status'


class ClientQuerySet(models.QuerySet):

    def actives(self, list_filter_dict):
        select = "SELECT id FROM Client WHERE status_id = 1"

        and_filter = ''
        params = []
        for key, list_items in list_filter_dict.items():
            if len(list_items) and list_items != ['']:
                # TO AVOID SQL INJECTION WE NEED TO PASS PARAMETERS IN FUNCTION RAW
                if key == 'city_slug':
                    params.append(list_items)
                    and_filter = f'{and_filter} AND city_id in (SELECT id from choices_city WHERE slug=%s)'
                    continue
                if key == 'genre_slug':
                    params.append(list_items)
                    and_filter = f'{and_filter} AND genre_id in (SELECT id from choices_genre WHERE slug=%s)'
                    continue
                else:
                    params.append(tuple(list_items))
                    and_filter = f'{and_filter} AND {key} in %s'

        order_by = 'ORDER BY profile_priority ASC'
        select_and_filter = f'{select} {and_filter} {order_by}'

        return self.raw(select_and_filter, params=params)


class ClientManager(models.Manager):
    def get_queryset(self):
        return ClientQuerySet(self.model, using=self._db)

    def actives(self, list_filter_dict={}):
        return self.get_queryset().actives(list_filter_dict)


# Create your models here.
class Client(models.Model):
    # SET MY OWN MANAGER
    objects = ClientManager()

    # SINGLE FIELDS
    slug = models.SlugField('slug', max_length=50, blank=True, unique=True)
    name = models.CharField('Nome', max_length=50, null=True, blank=True)
    fake_name = models.CharField('Apelido', max_length=50, null=True, blank=True)
    contact_email = models.EmailField('E-mail', unique=True, null=True)
    short_description = models.TextField('Pequena descrição', max_length=50, null=True, blank=True)
    description = models.TextField('Descrição', max_length=250, null=True, blank=True)
    phone = models.CharField('Celular', max_length=15, blank=True, null=True)
    image_profile = models.ImageField('Imagem de Perfil', upload_to=profile_upload_path, null=True, blank=True)
    image_thumb = models.ImageField('Thumb', upload_to=thumb_upload_path, null=True, blank=True)
    profile_priority = models.PositiveIntegerField('Prioridade do Profile', null=False)
    city = models.ForeignKey('ChoicesCity', verbose_name='Cidade', null=False, on_delete=models.DO_NOTHING)
    age = models.PositiveIntegerField('Idade', null=True, blank=True)
    weight = models.FloatField('Peso(kg)', null=True, blank=True)
    height = models.FloatField('Altura(m)', null=True, blank=True)
    bust = models.FloatField('Busto(cm)', null=True, blank=True)
    waist = models.FloatField('Cintura(cm)', null=True, blank=True)
    hip = models.FloatField('Quadril(cm)', null=True, blank=True)
    butt = models.FloatField('Bunda(cm)', null=True, blank=True)
    foot = models.FloatField('Pés', null=True, blank=True)
    service_charged = models.DecimalField('Cachê/Hr', max_digits=6, decimal_places=2, null=True, blank=True)

    # ONE TO ONE RELATIONS
    genre = models.ForeignKey('ChoicesGenre', verbose_name='Gênero', on_delete=models.DO_NOTHING, null=False)
    eye = models.ForeignKey('ChoicesEyeColor', verbose_name='Olhos', on_delete=models.DO_NOTHING, null=True, blank=True)
    hair = models.ForeignKey('ChoicesHairColor', verbose_name='Cabelos', on_delete=models.DO_NOTHING, null=True,
                             blank=True)
    ethnicity = models.ForeignKey('ChoicesEthnicity', verbose_name='Etnia', on_delete=models.DO_NOTHING, null=True,
                                  blank=True)
    status = models.ForeignKey('ChoicesStatus', verbose_name='Status', on_delete=models.DO_NOTHING, null=True,
                               blank=True)

    # MANY TO MANY RELATIONS
    languages = models.ManyToManyField('ChoicesLanguage',
                                       verbose_name='Idiomas',
                                       through='InterClientLanguages')

    customer_services = models.ManyToManyField('ChoicesCustomerService',
                                               verbose_name='Atendimentos',
                                               through='InterClientCustomerServices')

    places_accepted = models.ManyToManyField('ChoicesPlace',
                                             verbose_name='Lugares Aceitos',
                                             through='InterClientPlacesAccepted')

    payments_accepted = models.ManyToManyField('ChoicesPaymentAccepted',
                                               verbose_name='Pagamentos Aceitos',
                                               through='InterClientPaymentsAccepted')

    services_offered = models.ManyToManyField('ChoicesServicesOffered',
                                              verbose_name='Serviços Oferecidos',
                                              through='InterClientServicesOffered')

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('city.genre.client.details', args=[self.city.slug, self.genre.slug, self.slug])

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['genre', 'profile_priority']
        unique_together = ('city', 'genre', 'profile_priority')
        db_table = 'client'

    def __str__(self):
        return self.name


class ClientPhoto(models.Model):
    client = models.ForeignKey('Client', on_delete=models.CASCADE, null=False)
    photo = models.ImageField('Fotos', upload_to=photos_upload_path, null=False)
    order_priority = models.PositiveIntegerField('Prioridade da foto', null=False)

    class Meta:
        verbose_name = 'Foto'
        verbose_name_plural = 'Fotos'
        ordering = ['client', 'order_priority']
        unique_together = ('client', 'order_priority')
        db_table = 'client_photo'


class ClientVideo(models.Model):
    client = models.ForeignKey('Client', on_delete=models.CASCADE, null=False)
    video = models.FileField('Videos', upload_to=videos_upload_path, null=False)
    order_priority = models.PositiveIntegerField('Prioridade do Vídeo', null=False)

    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'
        ordering = ['client', 'order_priority']
        unique_together = ('client', 'order_priority')
        db_table = 'client_video'


class Highlight(models.Model):
    highlight_type_choices = (
        ("1", "top"),
        ("2", "left"),
        ("3", "right"),
        ("4", "bottom")
    )

    city = models.ForeignKey('ChoicesCity', on_delete=models.CASCADE, null=False, blank=False)
    genre = models.ForeignKey('ChoicesGenre', on_delete=models.CASCADE, null=False, blank=False)
    photo = models.ImageField('Foto destaque', upload_to=highlight_photo_upload_path, null=False, blank=False)
    highlight_type = models.CharField(max_length=50, choices=highlight_type_choices, null=False, blank=False)
    order_priority = models.PositiveIntegerField('Prioridade da foto', null=False, blank=False)
    client = models.ForeignKey('Client', on_delete=models.CASCADE, null=True, blank=True)
    url = models.CharField(max_length=255, null=False, blank=True)

    class Meta:
        verbose_name = 'Highlight'
        verbose_name_plural = 'Highlights'
        ordering = ['city', 'genre', 'highlight_type', 'order_priority']
        unique_together = ('city', 'genre', 'order_priority')
        db_table = 'highlight'


# INTERMEDIATE MODELS
class InterClientLanguages(models.Model):
    client = models.ForeignKey('Client', on_delete=models.CASCADE, null=False)
    language = models.ForeignKey('ChoicesLanguage', on_delete=models.DO_NOTHING, null=False)

    class Meta:
        verbose_name = 'Idioma'
        verbose_name_plural = 'Idiomas'
        ordering = ['client', 'language']
        unique_together = ('client', 'language')
        db_table = 'inter_client_languages'


class InterClientCustomerServices(models.Model):
    client = models.ForeignKey('Client', on_delete=models.CASCADE, null=False)
    customer_service = models.ForeignKey('ChoicesCustomerService', on_delete=models.DO_NOTHING, null=False)

    class Meta:
        verbose_name = 'inter_client_customer_services'
        verbose_name_plural = 'inter_client_customer_services'
        ordering = ['client', 'customer_service']
        unique_together = ('client', 'customer_service')
        db_table = 'inter_client_customer_services'


class InterClientPlacesAccepted(models.Model):
    client = models.ForeignKey('Client', on_delete=models.CASCADE, null=False)
    place = models.ForeignKey('ChoicesPlace', on_delete=models.DO_NOTHING, null=False)

    class Meta:
        verbose_name = 'inter_client_places_accepted'
        verbose_name_plural = 'inter_client_places_accepted'
        ordering = ['client', 'place']
        unique_together = ('client', 'place')
        db_table = 'inter_client_places_accepted'


class InterClientPaymentsAccepted(models.Model):
    client = models.ForeignKey('Client', on_delete=models.CASCADE, null=False)
    payment_accepted = models.ForeignKey('ChoicesPaymentAccepted', on_delete=models.DO_NOTHING, null=False)

    class Meta:
        verbose_name = 'inter_client_payments_accepted'
        verbose_name_plural = 'inter_client_payments_accepted'
        ordering = ['client', 'payment_accepted']
        unique_together = ('client', 'payment_accepted')
        db_table = 'inter_client_payments_accepted'


class InterClientServicesOffered(models.Model):
    client = models.ForeignKey('Client', on_delete=models.CASCADE, null=False)
    services_offered = models.ForeignKey('ChoicesServicesOffered', on_delete=models.DO_NOTHING, null=False)

    class Meta:
        verbose_name = 'inter_client_services_offered'
        verbose_name_plural = 'inter_client_services_offered'
        ordering = ['client', 'services_offered']
        unique_together = ('client', 'services_offered')
        db_table = 'inter_client_services_offered'
