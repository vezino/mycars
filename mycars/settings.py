"""
Django settings for mycars project.

Generated by 'django-admin startproject' using Django 1.10.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
# Parse database configuration from $DATABASE_URL
import dj_database_url
# To transform strings from environment variables to boolean values
import ast


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = 'jhh3(4=)4)r7geu=d2whloyu8a4&_wge&x=+tuz!@qc+sxoa#8'
SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = ast.literal_eval(os.environ['DEBUG_STATUS'])

#ALLOWED_HOSTS = []

# Check if we are in production
PRODUCTION = ast.literal_eval(os.environ['PRODUCTION'])
# Change allowed hosts accordingly
if PRODUCTION:
    ALLOWED_HOSTS = [os.environ['HEROKU_APP_NAME']+".herokuapp.com"]
else:
    #ALLOWED_HOSTS = [os.environ['ALLOWED_HOSTS']]
    ALLOWED_HOSTS = []
    

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # My apps
    'insurances.apps.InsurancesConfig',
    'drivers.apps.DriversConfig',
    'vehicle.apps.VehicleConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',  
    'whitenoise.middleware.WhiteNoiseMiddleware',  
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mycars.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        #'DIRS': [],
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'mycars.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
DATABASE_LOCAL =  ast.literal_eval(os.environ['DATABASE_LOCAL'])
DATABASE_USER =  os.environ['DATABASE_USER']
DATABASE_PASSWD = os.environ['DATABASE_PASSWD']
DATABASE_MYCARS = os.environ['DATABASE_MYCARS']
DATABASE_URL = os.environ['DATABASE_URL']

if DATABASE_LOCAL:
    DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
                'NAME': DATABASE_MYCARS,                      # Or path to database file if using sqlite3.
                # The following settings are not used with sqlite3:
                'USER': DATABASE_USER,
                'PASSWORD': DATABASE_PASSWD,
                'HOST': 'localhost',                      # Empty for localhost through domain sockets or           '127.0.0.1' for localhost through TCP.
                'PORT': '',                      # Set to empty string for default.
            }
        }
else:
    DATABASES = {'default': dj_database_url.config(default=DATABASE_URL)}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
#STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'
STATIC_URL = '/static/'
#ADMIN_MEDIA_PREFIX = '/static/admin/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    '/mycars/static/',
]

# Fixtures
FIXTURE_DIRS = (
   'fixtures/',
)

# Media Storage
#sMEDIA_ROOT="/mycars/media/"
#MEDIA_URL="media/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = os.path.join(BASE_DIR, 'media/')