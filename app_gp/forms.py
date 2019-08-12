from django.forms import forms, ImageField, CharField, ChoiceField, widgets, ModelChoiceField, ModelMultipleChoiceField, \
    modelformset_factory, \
    CheckboxSelectMultiple, MultiWidget, FileField, Select
from django.utils.html import format_html

from app_gp.utils.admin.widgets.PictureShow import PictureShowWidget
from django.forms.models import ModelForm
from app_gp.models import *
from django.forms.models import inlineformset_factory


class CityForm(forms.Form):
    state = ModelChoiceField(queryset=ChoicesStates.objects.all())
    city = ModelChoiceField(queryset=ChoicesCity.objects.filter(state=7))


class SearchClientForm(forms.Form):
    category = ModelChoiceField(queryset=ChoicesHairColor.objects.all(),
                                required=False,
                                widget=Select(attrs={'class': 'form-control'}))
    
    genre = ModelChoiceField(queryset=ChoicesGenre.objects.all(),
                             required=False,
                             widget=Select(attrs={'class': 'form-control'}))
    
    eye = ModelChoiceField(queryset=ChoicesEyeColor.objects.all(),
                           required=False,
                           widget=Select(attrs={'class': 'form-control'}))
    
    ethnicity = ModelChoiceField(queryset=ChoicesEthnicity.objects.all(),
                                 required=False,
                                 widget=Select(attrs={'class': 'form-control'}))

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

#
#         exclude = ()
#         fields = [
#             'name',
#             'fake_name',
# 'description',
# 'acting_cities',
# 'image_profile',
# 'age',
# 'service_charged',
# 'genre',
# 'ethnicity',
# 'customer_services',
# 'places_accepted',
# 'payments_accepted',
# 'services_offered',
# 'acting_cities',
# ]

# widgets = {
#     'customer_services': widgets.CheckboxSelectMultiple(),
#     'places_accepted': widgets.CheckboxSelectMultiple(),
#     'payments_accepted': widgets.CheckboxSelectMultiple(),
#     'services_offered': widgets.CheckboxSelectMultiple(),
# }
