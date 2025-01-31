from django.contrib import admin
from app_gp.forms import *
# from app_gp.utils.admin.client import *
from app_gp.utils.admin.city import *
from app_gp.utils.admin.customer_service import *
from app_gp.utils.admin.highlight import HighlightAdmin
from app_gp.utils.admin.neighborhoods import AdminNeighborhood


class InterClientActingCitiesAdmin(admin.ModelAdmin):
    # fieldsets = ('idClient.name', 'idCity.name')
    # list_display = ('city_id.name', )
    exclude = ()


# Register your models here.
# admin.site.register(Client)
admin.site.register(Client, ClientAdmin)
admin.site.register(Highlight, HighlightAdmin)

# ADMIN CHOICES
admin.site.register(ChoicesEthnicity)
admin.site.register(ChoicesGenre)
admin.site.register(ChoicesEyeColor)
admin.site.register(ChoicesCustomerService)
admin.site.register(ChoicesPlace)
admin.site.register(ChoicesPaymentAccepted)
admin.site.register(ChoicesServicesOffered)
admin.site.register(ChoicesStates)
admin.site.register(ChoicesNeighborhoods, AdminNeighborhood)
admin.site.register(ChoicesLanguage)
admin.site.register(ChoicesCity, AdminCity)


# ADMIN INTERMEDIATE
# admin.site.register(ModelInterClientCustomerServices)
# admin.site.register(ModelInterClientPlacesAccepted)
# admin.site.register(ModelInterClientPaymentsAccepted)
# admin.site.register(ModelInterClientServicesOffered)
# admin.site.register(InterClientActingCities, InterClientActingCitiesAdmin)
