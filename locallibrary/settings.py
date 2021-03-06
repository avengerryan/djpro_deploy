"""
Django settings for locallibrary project.

Generated by 'django-admin startproject' using Django 2.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'ztt9&4(@sp5t592)f!e!s3h7++m(1-h1zwzxyc-hp*)-=d1b^c'
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'cg#p$g+j9tax!#a3cup@1$8obt2_+&k3q+pmu)5%asj6yjpkag')

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
DEBUG = os.environ.get('DJANGO_DEBUG', '') != 'False'


# ALLOWED_HOSTS = []
# For deploying find the respective code for aws, azure, like below
ALLOWED_HOSTS = []
# ALLOWED_HOSTS = ['*', '127.0.0.1']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # This below object was created for us in /catalog/apps.py
    'catalog',
]

# For deploying the project/app on Heroku, and supplying static files we will
# be using whitenoise

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

ROOT_URLCONF = 'locallibrary.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
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

WSGI_APPLICATION = 'locallibrary.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'jangolocaldb',
            'USER': 'postgres',
            'PASSWORD': 'root',
            'HOST': 'localhost',
            'PORT': 5432,
        }
}



# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'mozidjangolocallibrary',
#         'USER': 'root',
#         'PASSWORD': 'raww',
#         'HOST': '',
#         'PORT': 5432,
#     }
# }

# My Notes:
    # HOST = '127.0.0.1' ip address instead of local host
    # port = '3306' for MySQL

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

# My Notes:
    # TIME_ZONE = 'UTC' Default value
    # Asia/Kolkata

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Redirect to home URL after login (Default redirects to /accounts/profile/)
LOGIN_REDIRECT_URL = '/'

# add to test email:
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# Heroku: Update database configuration from $DATABASE_URL
# import dj_database_url
#
# db_from_env = dj_database_url.config(conn_max_age = 500)
# DATABASES['default'].update(db_from_env)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

# the absolute path to the directory where collectstatic will collect static files
# for deployment.
STATIC_ROOT = BASE_DIR / 'staticfiles'

# os.path.join(BASE_DIR, 'staticfiles')


# the url to use when refering to static files (where they will be served from)
STATIC_URL = '/static/'


# static file serving
# http://whitenoise.evans.io/en/stable/django.html#django-middleware
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


