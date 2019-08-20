from app_gp.utils.admin.client import *


class TabularClientLanguages(admin.TabularInline):
    model = InterClientLanguages
    exclude = ()
    extra = 0
