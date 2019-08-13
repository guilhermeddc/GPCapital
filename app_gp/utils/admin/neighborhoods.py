from django.contrib import admin


class AdminNeighborhood(admin.ModelAdmin):
    list_display = ('city', 'neighborhood')
    list_filter = ('city',)
    search_fields = ('city', 'neighborhood')
    list_per_page = 15
