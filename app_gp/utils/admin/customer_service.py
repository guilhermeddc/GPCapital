from django.contrib import admin
from app_gp.forms import *
from app_gp.utils.admin.client import *


class TabularClientCustomerServices(admin.TabularInline):
    model = InterClientCustomerServices
    exclude = ()

    # def formfield_for_dbfield(self, db_field, **kwargs):
    #     attrs = {'size': 15}
    #     if db_field.attname == 'interest_level':
    #         attrs = {'size': 2}
    #     kwargs['widget'] = widgets.CheckboxSelectMultiple()
    #     return super(AdminInlineCustomerServices, self).formfield_for_dbfield(db_field, **kwargs)


class ModelFormCustomerService(ModelForm):

    class Meta:
        model = ChoicesCustomerService
        exclude = ()


# class AdminCustomerService(admin.ModelAdmin):
#     inlines = [TabularClientCustomerServices]
