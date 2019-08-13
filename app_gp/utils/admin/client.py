from django.contrib import admin
from django.forms import widgets, ModelForm, ModelChoiceField

# from app_gp.utils.admin.city import TabularClientCities
from app_gp.forms import ModelFormClient, ModelFormSit
from app_gp.models import *
from app_gp.utils.admin.photo import TabularClientPhotos
from app_gp.utils.admin.video import TabularClientVideos
from app_gp.utils.admin.widgets.PictureShow import PictureShowWidget


class SitsForm(ModelForm):
    
    class Meta:
        model = InterCitySit
        exclude = ()
        
        
class TabularSits(admin.TabularInline):
    model = InterCitySit
    # form = SitsForm
    raw_id_fields = ('city', )


class ClientAdmin(admin.ModelAdmin):
    # form = ModelFormClient
    inlines = [TabularClientPhotos, TabularClientVideos, TabularSits]
    # change_form_template = 'admin/change2.html'
    list_display = ('slug', 'fake_name', 'name', 'genre', 'age', 'hair', 'eye', 'ethnicity', 'status', 'weight', 'height', 'bust', 'waist', 'butt')
    list_filter = ('genre', 'hair', 'eye', 'ethnicity')
    # readonly_fields = ('slug', )
    
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
    # def get_formsets_with_inlines(self, request, obj=None):
    #     return super(ClientAdmin, self).get_formsets_with_inlines(request, obj)
    #
    # def get_inline_formsets(self, request, formsets, inline_instances, obj=None):
    #     return super(ClientAdmin, self).get_inline_formsets(request, formsets, inline_instances, obj)
