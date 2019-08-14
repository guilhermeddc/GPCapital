from django.contrib import admin
from app_gp.forms import *


# class CityForm(ModelForm):
#     class Meta:
#         model = InterClientActingCities
#         exclude = ()


# class TabularClientCities(admin.TabularInline):
#     model = InterClientActingCities
#     extra = 0
#     exclude = ()
    
    
    # form = CityForm
    # fields = ('city_set_name', )
    # raw_id_fields = ('city.name', )
    # autocomplete_fields = ('city', )


class AdminCity(admin.ModelAdmin):
    list_display = ('id', 'city', 'state')
    list_filter = ('state',)
    search_fields = ('city', )
    list_per_page = 15
