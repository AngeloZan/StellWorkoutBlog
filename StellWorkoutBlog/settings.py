"""
Django settings for StellWorkoutBlog project.

Generated by 'django-admin startproject' using Django 3.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path

import os
import environ

# iniciando variaveis de ambiente
env = environ.Env()
environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
if env('DEBUG'):
    DEBUG = env('DEBUG') == 'True'
else:
    DEBUG = True

if DEBUG:
    SECRET_KEY = ')($ryv@%&kirl4w@=77grhc2d(wlr#z)c7o#9h8fnp2orp&3pv'
else:
    SECRET_KEY = env('SECRET_KEY')

if not DEBUG:
    ALLOWED_HOSTS = ['stellworkout.com', 'www.stellworkout.com']

else:
    ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog.apps.BlogConfig',
    'account.apps.AccountConfig',
    'pages.apps.PagesConfig',
    'django_cleanup.apps.CleanupConfig',
    'phonenumber_field',
    'django_countries',
    'django.contrib.postgres',
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

ROOT_URLCONF = 'StellWorkoutBlog.urls'

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

# Custom user model
AUTH_USER_MODEL = 'account.Account'

WSGI_APPLICATION = 'StellWorkoutBlog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASS'),
        'HOST': env('DB_HOST'),
        'PORT': env('DB_PORT'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
if not DEBUG:
    STATIC_ROOT = os.path.join(BASE_DIR, "static/")
else:
    STATICFILES_DIRS = (os.path.join('static'),)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Email stuff
SEND_MAILS = env('SEND_MAILS')

# informacoes armazenadas em variaveis de ambiente
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
MAILER_EMAIL_BACKEND = EMAIL_BACKEND
EMAIL_HOST = env('EMAIL_HOST')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_USE_TLS = env('EMAIL_USE_TLS')
EMAIL_PORT = env('EMAIL_PORT')
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
CONFIRMATION_FROM_EMAIL = EMAIL_HOST_USER
POST_NOTIFICATION_EMAIL = EMAIL_HOST_USER
RESET_PASSWORD_EMAIL = EMAIL_HOST_USER
FEEDBACK_EMAIL_SENDER = EMAIL_HOST_USER
FEEDBACK_EMAIL_RECEIVER = EMAIL_HOST_USER
AJUDA_EMAIL_SENDER = EMAIL_HOST_USER
AJUDA_EMAIL_RECEIVER = EMAIL_HOST_USER

# phene numbers settings
PHONENUMBER_DB_FORMAT = 'NATIONAL'
PHONENUMBER_DEFAULT_REGION = 'BR'

# SSL stuff
SSL = env('SSL') # true when using a ssl certificate

if SSL:
    # HTTPS settings
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_SSL_REDIRECT = True

    # HSTS settings
    SECURE_HSTS_SECONDS = 31536000 # 1 yr
    SECURE_HSTS_PRELOAD = True
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
