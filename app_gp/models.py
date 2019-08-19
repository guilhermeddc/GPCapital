import random
from django.db import models
import os

UPLOAD_PHOTOS_PATH = 'Media'
UPLOAD_VIDEOS_PATH = 'Media'


class ChoicesEthnicity(models.Model):
    ethnicity = models.CharField('Etnia', max_length=50, null=False, blank=False)

    class Meta:
        verbose_name = 'Etnia'
        verbose_name_plural = 'Etnias'
        ordering = ['ethnicity']
        db_table = 'choices_ethnicity'

    def __str__(self):
        return self.ethnicity


class ChoicesGenre(models.Model):
    genre = models.CharField('Gênero', max_length=50, null=False, blank=False)

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


class ChoicesCity(models.Model):
    city = models.CharField('Cidade', max_length=255, null=False)
    state = models.CharField('UF', max_length=5, null=False)
    cep = models.CharField('Cep', max_length=10, null=True)
    ibge_code = models.CharField('Código IBGE', max_length=255, null=False)
    area = models.FloatField('Area', null=True)
    subordinate_municipality = models.IntegerField('Município subordinado', null=False)

    class Meta:
        verbose_name = 'Cidade'
        verbose_name_plural = 'Cidades'
        ordering = ['state', 'city']
        db_table = 'choices_city'

    def __str__(self):
        return f'{self.state}-{self.city}'


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


def get_basic_path(instance):
    return f'Media/{instance.genre}/{instance.name}'


def profile_upload_path(instance, filename):
    basic_path = get_basic_path(instance)
    base_name = os.path.basename(filename)
    path = f'Media/{basic_path}/profile/{base_name}'
    return path


def thumb_upload_path(instance, filename):
    basic_path = get_basic_path(instance)
    base_name = os.path.basename(filename)
    name, ext = os.path.splitext(base_name)
    # Rename to filename_thumb.jpg
    new_name = f'{name}_thumb{ext}'
    path = f'{basic_path}/profile/{new_name}'
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
                params.append(tuple(list_items))
                and_filter = f' {and_filter} AND {key} in %s'

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
    short_description = models.TextField('Pequena descrição', max_length=50, null=True, blank=True)
    description = models.TextField('Descrição', max_length=250, null=True, blank=True)
    image_profile = models.ImageField('Imagem de Perfil', upload_to=profile_upload_path, null=True, blank=True)
    image_thumb = models.ImageField('Thumb', upload_to=thumb_upload_path, null=True, blank=True)
    profile_priority = models.PositiveIntegerField('Prioridade do Profile', null=False)
    city = models.ForeignKey('ChoicesCity', verbose_name='Cidade', null=False, on_delete=models.DO_NOTHING)
    age = models.PositiveIntegerField('Idade', null=True, blank=True)
    weight = models.FloatField('Peso(kg)', null=True, blank=True)
    height = models.FloatField('Altura(m)', null=True, blank=True)
    bust = models.FloatField('Busto(cm)', null=True, blank=True)
    waist = models.FloatField('Cintura(cm)', null=True, blank=True)
    butt = models.FloatField('Bunda(cm)', null=True, blank=True)
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

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['genre', 'profile_priority']
        unique_together = ('city', 'genre', 'profile_priority')
        db_table = 'client'

    def __str__(self):
        return self.name


class ClientPhoto(models.Model):
    client = models.ForeignKey('Client', on_delete=models.DO_NOTHING, null=False)
    photo = models.ImageField('Fotos', upload_to=UPLOAD_PHOTOS_PATH, null=False)
    order_priority = models.PositiveIntegerField('Prioridade da foto', null=False)

    class Meta:
        verbose_name = 'Foto'
        verbose_name_plural = 'Fotos'
        ordering = ['client', 'order_priority']
        unique_together = ('client', 'order_priority')
        db_table = 'client_photo'


class ClientVideo(models.Model):
    client = models.ForeignKey('Client', on_delete=models.DO_NOTHING, null=False)
    video = models.FileField('Videos', upload_to=UPLOAD_VIDEOS_PATH, null=False)
    order_priority = models.PositiveIntegerField('Prioridade do Vídeo', null=False)

    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'
        ordering = ['client', 'order_priority']
        unique_together = ('client', 'order_priority')
        db_table = 'client_video'


# INTERMEDIATE MODELS
class InterClientCustomerServices(models.Model):
    client = models.ForeignKey('Client', on_delete=models.DO_NOTHING, null=False)
    customer_service = models.ForeignKey('ChoicesCustomerService', on_delete=models.DO_NOTHING, null=False)

    class Meta:
        verbose_name = 'inter_client_customer_services'
        verbose_name_plural = 'inter_client_customer_services'
        ordering = ['client', 'customer_service']
        unique_together = ('client', 'customer_service')
        db_table = 'inter_client_customer_services'


class InterClientPlacesAccepted(models.Model):
    client = models.ForeignKey('Client', on_delete=models.DO_NOTHING, null=False)
    place = models.ForeignKey('ChoicesPlace', on_delete=models.DO_NOTHING, null=False)

    class Meta:
        verbose_name = 'inter_client_places_accepted'
        verbose_name_plural = 'inter_client_places_accepted'
        ordering = ['client', 'place']
        unique_together = ('client', 'place')
        db_table = 'inter_client_places_accepted'


class InterClientPaymentsAccepted(models.Model):
    client = models.ForeignKey('Client', on_delete=models.DO_NOTHING, null=False)
    payment_accepted = models.ForeignKey('ChoicesPaymentAccepted', on_delete=models.DO_NOTHING, null=False)

    class Meta:
        verbose_name = 'inter_client_payments_accepted'
        verbose_name_plural = 'inter_client_payments_accepted'
        ordering = ['client', 'payment_accepted']
        unique_together = ('client', 'payment_accepted')
        db_table = 'inter_client_payments_accepted'


class InterClientServicesOffered(models.Model):
    client = models.ForeignKey('Client', on_delete=models.DO_NOTHING, null=False)
    services_offered = models.ForeignKey('ChoicesServicesOffered', on_delete=models.DO_NOTHING, null=False)

    class Meta:
        verbose_name = 'inter_client_services_offered'
        verbose_name_plural = 'inter_client_services_offered'
        ordering = ['client', 'services_offered']
        unique_together = ('client', 'services_offered')
        db_table = 'inter_client_services_offered'
