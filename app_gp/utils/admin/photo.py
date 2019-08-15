from django.contrib import admin
from app_gp.forms import *
from app_gp.utils.admin.widgets.PictureShow import PictureShowWidget


class PhotoForm(ModelForm):

    class Meta:
        model = ClientPhoto
        fields = ('photo', )
        widgets = {
            'photo': PictureShowWidget()
        }


class TabularClientPhotos(admin.TabularInline):
    model = ClientPhoto
    form = PhotoForm
    extra = 0
    # template = 'admin/tabular.html'







