
from django.contrib.messages import constants as messages
import django_heroku

import os


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(a2!(=3rx+b%^@^(e#c&7qy@e30vwppdo72y3sve7ba8^mw&)0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    # 'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.humanize',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'articles',
    'accounts',
    'crispy_forms',
    'mptt',
    'tinymce',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]


ROOT_URLCONF = 'firstdev.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'firstdev.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'GMT'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/


STATIC_URL = '/static/'
MEDIA_URL = '/media/'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

MEDIA_ROOT = "C:/Users/sa966/OneDrive/Desktop/projects/media/djangoblog"
STATIC_ROOT = "C:/Users/sa966/OneDrive/Desktop/projects/static/djangoblog"

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static", "static_root"),
]

MESSAGE_TAGS = {
    messages.ERROR: 'danger'
}

# user model
AUTH_USER_MODEL = 'accounts.CustomUser'

# Email
EMAIL_HOST = 'smtp.gmail.com' # os.environ.get("EMAIL_HOST")
EMAIL_USE_TLS = True # os.environ.get("EMAIL_USE_TLS")
EMAIL_HOST_USER = 'codeforces221405@gmail.com' # os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = 'pcVAeA*#$442' # os.environ.get("EMAIL_HOST_PASSWORD")
EMAIL_PORT = 587 # os.environ.get("EMAIL_PORT")

django_heroku.settings(locals())
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
