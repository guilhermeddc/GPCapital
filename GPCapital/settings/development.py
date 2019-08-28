from .base import *

SECRET_KEY = '2ggw4rwb6&mzh0jdfxvmkdi)io%8emyv3*u8me8rk455v^ery5'

DEBUG = True

ALLOWED_HOSTS = ['gpcapital-dev.sa-east-1.elasticbeanstalk.com', '127.0.0.1']

INSTALLED_APPS += [
    'storages',
]

DATABASES['default'].update({
    'NAME': os.environ['RDS_DB_NAME'],
    'USER': os.environ['RDS_USERNAME'],
    'PASSWORD': os.environ['RDS_PASSWORD'],
    'HOST': os.environ['RDS_HOSTNAME'],
    'PORT': os.environ['RDS_PORT'],
})


# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'myapp', 'templates', 'static')
# ]

STATICFILES_LOCATION = 'static'
MEDIAFILES_LOCATION = 'media'

AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']

AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'


STATICFILES_STORAGE = 'GPCapital.customS3.utils.PublicStaticStorage'
STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
# STATIC_ROOT = '/static/'

DEFAULT_FILE_STORAGE = 'GPCapital.customS3.utils.PublicMediaStorage'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
# MEDIA_ROOT = '/media/'

