from django.contrib import admin
from django.forms import widgets, ModelForm, ModelChoiceField, fields

# from app_gp.utils.admin.city import TabularClientCities
from app_gp.forms import ModelFormClient, ModelFormSit
from app_gp.models import *
from app_gp.utils.admin.photo import TabularClientPhotos
from app_gp.utils.admin.video import TabularClientVideos
from app_gp.utils.admin.widgets.PictureShow import PictureShowWidget


class TabularSits(admin.TabularInline):
    model = ClientCitySit
    fields = ('city', 'sit_number')
    raw_id_fields = ('city', )
    exclude = ()


class TabularClientCustomerServices(admin.TabularInline):
    model = InterClientCustomerServices
    exclude = ()
    extra = 0


class ClientAdmin(admin.ModelAdmin):
    # form = ModelFormClient
    inlines = [TabularClientCustomerServices, TabularClientPhotos, TabularClientVideos, TabularSits]
    # change_form_template = 'admin/change2.html'
    list_display = ('slug', 'fake_name', 'name', 'city', 'profile_priority', 'genre', 'age', 'hair', 'eye',
                    'ethnicity', 'status', 'weight', 'height', 'bust', 'waist', 'butt')
    list_filter = ('status', 'genre', 'hair', 'eye', 'ethnicity')
    readonly_fields = ('slug', )
    
    # fields = ('slug', 'fake_name', 'name')
    exclude = ()
    # fieldsets = (
    #     ('Perfil', {
    #         'fields': ('name', 'fake_name', 'image_profile', 'age', 'genre', 'ethnicity')
    #     }),
    #     ('Detalhes', {
    #         'fields': ('customer_services', 'places_accepted', 'payments_accepted', 'services_offered')
    #     }),
    # )

    # def sit_number(self, obj):
    #     return obj.client_city_sit.sit_number
    #
    # def city(self, obj):
    #     return obj.client_city_sit.city.city
    
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.attname == 'image_profile':
            kwargs['widget'] = PictureShowWidget()

        return super(ClientAdmin, self).formfield_for_dbfield(db_field, **kwargs)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.attname in ('customer_services', 'places_accepted', 'payments_accepted', 'services_offered'):
            kwargs['widget'] = widgets.CheckboxSelectMultiple
            # kwargs['widget'] = widgets.CheckboxSelectMultiple(attrs={'class': 'form-check form-check-inline'})

        return super(ClientAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)

    # def formfield_for_foreignkey(self, db_field, request, **kwargs):
    #     return super(ClientAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
    #
    # def formfield_for_choice_field(self, db_field, request, **kwargs):
    #     return super(ClientAdmin, self).formfield_for_choice_field(db_field, request, **kwargs)
    #
    # def get_fields(self, request, obj=None):
    #     return super(ClientAdmin, self).get_fields(request, obj)
    #
    def get_formsets_with_inlines(self, request, obj=None):
        return super(ClientAdmin, self).get_formsets_with_inlines(request, obj)

    def get_inline_formsets(self, request, formsets, inline_instances, obj=None):
        return super(ClientAdmin, self).get_inline_formsets(request, formsets, inline_instances, obj)
