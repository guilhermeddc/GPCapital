from django.forms import forms, ImageField, CharField, ChoiceField, widgets, ModelChoiceField, ModelMultipleChoiceField, modelformset_factory, \
    CheckboxSelectMultiple, MultiWidget, FileField
from django.utils.html import format_html

from app_gp.utils.admin.widgets.PictureShow import PictureShowWidget
from django.forms.models import ModelForm
from app_gp.models import *
from django.forms.models import inlineformset_factory


# class PictureWidget(widgets.Widget):
#     def render(self, name, value, attrs=None, renderer=None):
#         html = super(PictureWidget, self).render()
#         return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
#             url=value.url,     # obj.image_profile.url,
#             width=250,   # obj.image_profile.width,
#             height=300))     # obj.image_profile.height,))

# class ModelFormClient(ModelForm):
#     image_profile = ImageField(widget=PictureShow(), required=False)
#
#     class Meta:
#         model = Client
#
#         exclude = ()
        # fields = [
        #     'name',
        #     'acting_cities',
        #     'fake_name',
        #     'description',
        #     'acting_cities',
        #     'image_profile',
        #     'age',
        #     'service_charged',
        #     'genre',
        #     'ethnicity',
        #     # 'customer_services',
        #     'places_accepted',
        #     'payments_accepted',
        #     'services_offered',
        #     # 'acting_cities',
        # ]

        # widgets = {
        #     'customer_services': widgets.CheckboxSelectMultiple(),
        #     'places_accepted': widgets.CheckboxSelectMultiple(),
        #     'payments_accepted': widgets.CheckboxSelectMultiple(),
        #     'services_offered': widgets.CheckboxSelectMultiple(),
        # }



