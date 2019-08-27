from django.forms import forms, ImageField, CharField, ChoiceField, widgets, ModelChoiceField, ModelMultipleChoiceField, \
    modelformset_factory, \
    CheckboxSelectMultiple, MultiWidget, FileField, Select, SelectMultiple
from django.utils.html import format_html

from app_gp.utils.admin.widgets.PictureShow import PictureShowWidget
from django.forms.models import ModelForm
from app_gp.models import *
from django.forms.models import inlineformset_factory


class CityChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return f'{obj.state}-{obj.city}'


class CitySearchForm(forms.Form):
    city = CityChoiceField(queryset=ChoicesCity.objects.worked_cities(), label=False,
                           initial=True,
                           required=True,
                           to_field_name='slug',
                           widget=Select(attrs={
                               'class': 'into-square mdb-select colorful-select dropdown-dark md-form wow fadeIn',
                               'data-wow-delay': '0.4s',
                               'is_hidden': 'False',
                               'searchable': "ESCOLHA SUA CIDADE:"}))


class SearchClientForm(forms.Form):
    category = ModelChoiceField(queryset=ChoicesHairColor.objects.all(), empty_label=None,
                                initial=False,
                                required=False,
                                widget=SelectMultiple(
                                    attrs={
                                        'class': 'col-12 mdb-select colorful-select dropdown-dark md-form wow fadeIn',
                                        'data-wow-delay': '0.4s'}))

    genre = ModelChoiceField(queryset=ChoicesGenre.objects.all(), empty_label=None,
                             initial=False,
                             required=False,
                             widget=SelectMultiple(
                                 attrs={
                                     'class': 'col-12 mdb-select colorful-select dropdown-dark md-form wow fadeIn',
                                     'data-wow-delay': '0.4s'}))

    eye = ModelChoiceField(queryset=ChoicesEyeColor.objects.all(), empty_label=None,
                           initial=False,
                           required=False,
                           widget=SelectMultiple(
                               attrs={'class': 'col-12 mdb-select colorful-select dropdown-dark md-form wow fadeIn',
                                      'data-wow-delay': '0.4s'}))

    ethnicity = ModelChoiceField(queryset=ChoicesEthnicity.objects.all(), empty_label=None,
                                 initial=False,
                                 required=False,
                                 widget=SelectMultiple(
                                     attrs={
                                         'class': 'col-12 mdb-select colorful-select '
                                                  'dropdown-dark md-form wow fadeIn',
                                         'data-wow-delay': '0.4s'}))

# class PictureWidget(widgets.Widget):
#     def render(self, name, value, attrs=None, renderer=None):
#         html = super(PictureWidget, self).render()
#         return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
#             url=value.url,     # obj.image_profile.url,
#             width=250,   # obj.image_profile.width,
#             height=300))     # obj.image_profile.height,))


# class ModelFormClient(ModelForm):
#
#     class Meta:
#         model = Client
#         # exclude = ()
#         fields = [
#             'name',
#             'fake_name',
#             'description',
#             'image_profile',
#             'client_city_sit_order',
#             'age',
#             'service_charged',
#             'genre',
#             'ethnicity',
#             'customer_services',
#             'places_accepted',
#             'payments_accepted',
#             'services_offered',
#             'acting_cities',
#         ]

# widgets = {
#     'customer_services': widgets.CheckboxSelectMultiple(),
#     'places_accepted': widgets.CheckboxSelectMultiple(),
#     'payments_accepted': widgets.CheckboxSelectMultiple(),
#     'services_offered': widgets.CheckboxSelectMultiple(),
# }
