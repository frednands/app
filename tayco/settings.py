
from django.contrib.messages import constants as messages
from pathlib import Path
import os
import django_heroku
import sys
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

LOGIN_URL ='/user/login/'

SECRET_KEY = 'django-insecure-juxjupgae-7b^fl9)4et+1588zbh7usv0by#r7g(jkp(1#r%z-'

DEBUG = True


ALLOWED_HOSTS = ['*']

AUTH_USER_MODEL ='authentification.User'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'authentification',
    'project',
    'import_export',
    'client',
    'event',
    'post',
    
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

ROOT_URLCONF = 'tayco.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR,'template'],
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

WSGI_APPLICATION = 'tayco.wsgi.application'

# Host
# c7gljno857ucsl.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com
# Database
# d47r1acfnabqms
# User
# u394reorqkj6vh
# Port
# 5432
# Password
# paef43e8a3f355c6ba046105cfd90a3982ed0e017cc39554938d45ef633e0a2ca
# URI
# postgres://u394reorqkj6vh:paef43e8a3f355c6ba046105cfd90a3982ed0e017cc39554938d45ef633e0a2ca@c7gljno857ucsl.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd47r1acfnabqms',
        'USER': 'u394reorqkj6vh',
        'PASSWORD': 'paef43e8a3f355c6ba046105cfd90a3982ed0e017cc39554938d45ef633e0a2ca',
        'HOST': 'c7gljno857ucsl.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com',
        'PORT': '5432'
    }
}


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




LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True



STATIC_URL = 'static/'
STATICFILES_DIRS=[BASE_DIR,'tayco/static']


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
LOGIN_REDIRECT_URL = '/dashboard'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_FROM = 'info@tayco.org.tz'
EMAIL_HOST_USER = 'sfrednand@gmail.com'
EMAIL_FROM_USER = 'info@tayco.org.tz'
EMAIL_HOST_PASSWORD ='hwqbpharsqpflibb'
EMAIL_PORT = 587
EMAIL_USE_TLS = True


MESSAGE_TAGS = {
    messages.ERROR: "danger",
    
}
django_heroku.settings(locals())
