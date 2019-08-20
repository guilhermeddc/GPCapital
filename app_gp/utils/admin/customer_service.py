from django.contrib import admin
from app_gp.forms import *
from app_gp.utils.admin.client import *


class TabularClientCustomerServices(admin.TabularInline):
    model = InterClientCustomerServices
    exclude = ()


class ModelFormCustomerService(ModelForm):

    class Meta:
        model = ChoicesCustomerService
        exclude = ()


# class AdminCustomerService(admin.ModelAdmin):
#     inlines = [TabularClientCustomerServices]
