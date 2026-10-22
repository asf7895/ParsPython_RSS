#from settings import *

# Django settings for pr1 project.

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


DEBUG = True

DATABASES = {
#    'default': {
        #'ENGINE': 'django.db.backends.', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
#        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
#        'NAME': 'postgres',                      # Or path to database file if using sqlite3.
#        'USER': 'postgres',                      # Not used with sqlite3.
#        'PASSWORD': 'Fghty342',                  # Not used with sqlite3.
#        'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
#        'PORT': '5432',                      # Set to empty string for default. Not used with sqlite3.
#    }

#    'default': {
#        'ENGINE': 'django.db.backends.mysql',
#        'NAME': 'exmp2',
#        'USER': 'asf',
#        'PASSWORD': 'asf78tgh',
#        'HOST': 'localhost',  # или IP-адрес сервера БД
#        'PORT': '3306',
#    }

    'default': {
         'ENGINE': 'django.db.backends.{}'.format(os.getenv('DATABASE_ENGINE', 'mysql')),
         'NAME': os.getenv('DB_NAME', 'exmp2'),
         'USER': os.getenv('DB_USER', 'asf'),
         'PASSWORD': os.getenv('DB_PASSWORD', 'asf78tgh'),
         'HOST': 'db',
         'PORT': os.getenv('DB_PORT', '3306'),
    }


}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.4/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ["127.0.0.1", "localhost"]


# List of finder classes that know how to find static files in
# various locations.
# Make this unique, and don't share it with anybody.
SECRET_KEY = 'wf#k&amp;3gp!8@)k4+r9v9#%npu(o8h8eq5s%!b^)k1^pfb$rr60m'



INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'pr1.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ["web//app1//templates"],
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

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'pr1.wsgi.application'

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATICFILES_DIRS = ['web//app1//static/']

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


