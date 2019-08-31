from django.contrib import admin


class HighlightAdmin(admin.ModelAdmin):
    list_display = ('city', 'genre', 'highlight_type', 'order_priority')
    list_filter = ('genre', 'highlight_type')
    list_per_page = 15
    raw_id_fields = ('city', 'client')
    # fields = ('slug', 'fake_name', 'name')
    exclude = ()
