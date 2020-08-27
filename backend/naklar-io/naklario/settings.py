"""
Django settings for lernroulette project.

Generated by 'django-admin startproject' using Django 3.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = "12345678"

BBB_SHARED = "12345678"
BBB_URL = "https://bbb.naklar.io"

# configure for production, see https://docs.djangoproject.com/en/3.0/ref/settings/#email-backend
EMAIL_HOST = "smtpd"
EMAIL_PORT = "1025"

DATA_UPLOAD_MAX_MEMORY_SIZE = 10485760  # 10mb


API_HOST = "http://localhost:8000"
HOST = "http://localhost:4000"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

CORS_ORIGIN_WHITELIST = [
    "http://localhost:4000",
]

# Set custom user model
AUTH_USER_MODEL = 'account.CustomUser'
SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Token': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        }
    },
    'SECURITY_REQUIREMENTS': [
        {'Token': []},
    ],
    'REFETCH_SCHEMA_WITH_AUTH': True,
    'PERSIST_AUTH': True
}

# Rest framework
REST_FRAMEWORK = {
    'DEFAULT_PARSER_CLASSES': [
         'djangorestframework_camel_case.parser.CamelCaseFormParser',
        'djangorestframework_camel_case.parser.CamelCaseMultiPartParser',
        'djangorestframework_camel_case.parser.CamelCaseJSONParser',
        # 'rest_framework.parsers.JSONParser',
        #        'rest_framework.parsers.XMLParser',
    ],
    'DEFAULT_RENDERER_CLASSES': [
        'djangorestframework_camel_case.render.CamelCaseJSONRenderer',
        'djangorestframework_camel_case.render.CamelCaseBrowsableAPIRenderer',
        # 'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
      
        #        'rest_framework_xml.renderers.XMLRenderer',
    ],
    'JSON_UNDERSCOREIZE': {
        'no_underscore_before_number': True,
    },

    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'knox.auth.TokenAuthentication',
    ],
    'UPLOADED_FILES_USE_URL': True,
}

REST_KNOX = {
    "TOKEN_TTL": None
}

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'knox',
    # 3rd party libs
    'channels',
    'drf_yasg',
    'corsheaders',
    'drf_base64',
    'django_celery_beat',
    # our components
    'account',
    'call',
    'roulette',
    'landing',
    'notify',
    # 3rd party that needs to load last
    'post_office',
    'push_notifications',
    'multiselectfield'
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'naklario.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
            'filters': ['require_debug_true'],
            'level': 'INFO'
        }
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO'
    },
}

WSGI_APPLICATION = 'naklario.wsgi.application'

ASGI_APPLICATION = 'naklario.routing.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'de-de'

TIME_ZONE = 'Europe/Berlin'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = '/opt/static/'


MEDIA_URL = '/media/'
MEDIA_ROOT = '/opt/media/'

# Celery:
CELERY_APP = "naklario.celery"
CELERY_BROKER_URL = "amqp://rabbitmq"

CELERY_ACCEPT_CONTENT = ['json', 'pickle']

# For reverse nginx proxy, we forward this. make sure this is being forwarded for all!
USE_X_FORWARDED_HOST = True


# as we're using CELERY
POST_OFFICE = {
    'DEFAULT_PRIORITY': 'now'
}

try:
    from .settings_local import *
except ImportError:
    print("Unable to find settings_local.py! We need a configuration for this")