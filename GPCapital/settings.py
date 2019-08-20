"""
Django settings for GPCapital project.

Generated by 'django-admin startproject' using Django 2.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# GP APP DIR PATH's
GP_DIR = os.path.join(BASE_DIR, 'app_gp')
TEMPLATES_DIR = (
    os.path.join(GP_DIR, 'templates')
)
GP_STATIC_DIR = os.path.join(GP_DIR, 'static')

#   dumpdata app_gp.Client --format=json --indent 2 -o app_gp/fixtures/initial_data.json
FIXTURE_DIRS = (
   os.path.join(GP_DIR, 'fixtures'),
)

# GP_CLIENT_PHOTOS_DIR = os.path.join(GP_STATIC_DIR, 'models_photos')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2ggw4rwb6&mzh0jdfxvmkdi)io%8emyv3*u8me8rk455v^ery5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app_gp',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'GPCapital.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'GPCapital.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': dict(ENGINE='django.db.backends.postgresql_psycopg2', NAME='gpcapital', USER='postgres',
                    PASSWORD='trismegistos', HOST='localhost', PORT='5432')
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

# In the INSTALLED_APPS the 'django.contrib.staticfiles' will serve all static files and the URL tag will begin with
# STATIC_URL
STATIC_URL = '/static/'

# That's where files get collected automatically after you run manage.py collectstatic
# This will export all static files stored in $APP/static/ and STATICFILES_DIRS to STATIC_ROOT
# STATIC_ROOT = os.path.join(BASE_DIR, "allstaticfiles")

# In the INSTALLED_APPS the 'django.contrib.staticfiles' will look for Static files that are stored in $APP/static/
# BUT if you want to look in another path you need to put in STATICFILES_DIRS
# STATICFILES_DIRS = [
# os.path.join(GP_DIR, 'my_static_file_path')
# ]

MEDIA_URL = '/media/'
