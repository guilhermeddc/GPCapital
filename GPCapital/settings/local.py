from .base import *

SECRET_KEY = '2ggw4rwb6&mzh0jdfxvmkdi)io%8emyv3*u8me8rk455v^ery5'

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

DATABASES['default'].update({
    'NAME': 'gpcapital',
    'USER': 'postgres',
    'PASSWORD': 'trismegistos',
    'HOST': 'localhost',
    'PORT': '5432',
})


STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'

# In the INSTALLED_APPS the 'django.contrib.staticfiles' will serve all static files and the URL tag will begin with
# STATIC_URL
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# THUMBNAIL_FILE_STORAGE = DEFAULT_FILE_STORAGE

# That's where files get collected automatically after you run manage.py collectstatic
# This will export all static files stored in $APP/static/ and STATICFILES_DIRS to STATIC_ROOT
# STATIC_ROOT = os.path.join(BASE_DIR, "www", "static")

# In the INSTALLED_APPS the 'django.contrib.staticfiles' will look for Static files that are stored in $APP/static/
# BUT if you want to look in another path you need to put in STATICFILES_DIRS
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'myapp', 'templates', 'static')
# ]

