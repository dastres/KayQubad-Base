import os
import environ
from pathlib import Path
from datetime import timedelta
from django.utils.translation import gettext_lazy as _

env = environ.Env(DEBUG=(bool, False))

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    # main apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 3rd party
    'rest_framework',
    'django_filters',
    'drf_spectacular',
    'drf_spectacular_sidecar',
    'ckeditor',
    'ckeditor_uploader',
    'modeltranslation',

    'django_seed',  # TODO:for develop

    # my app
    'accounts.apps.AccountsConfig',
    'utils.apps.UtilsConfig',
    'forms.apps.FormsConfig',
    'blog.apps.BlogConfig',
    'project.apps.ProjectConfig',
    'portfolio.apps.PortfolioConfig',
    'page.apps.PageConfig',
    'dastres.apps.DastresConfig',
    'marketing.apps.MarketingConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware'
]

ROOT_URLCONF = 'kayqubad_core.urls'

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

WSGI_APPLICATION = 'kayqubad_core.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

if env('DB_ENGINE') != 'postgresql':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': env('DB_NAME'),
            'USER': env('DB_USER'),
            'PASSWORD': env('DB_PASSWORD'),
            'HOST': env('DB_HOST'),
            'PORT': env('DB_PORT'),
        }
    }

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'fa'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Config MultiLanguage
LANGUAGES = (
    ('en', _('English')),
    ('fa', _('Persian')),
)

LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale/')]

# Config django-modeltranslation
MODELTRANSLATION_DEFAULT_LANGUAGE = 'fa'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
MEDIA_URL = 'media/'

STATIC_ROOT = BASE_DIR / 'static'
MEDIA_ROOT = BASE_DIR / 'media'

STATICFILES_DIRS = [
    BASE_DIR / "kayqubad_core" / "assets",
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# CustomUser Config
AUTH_USER_MODEL = 'accounts.CustomUser'

# Config JWT
SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('JWT',),
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
}

# DRF Config
REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ]
}

# Config drf-spectacular
SPECTACULAR_SETTINGS = {
    'TITLE': 'KeyQubad Base',
    'DESCRIPTION': 'Dastres Base',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    'SWAGGER_UI_DIST': 'SIDECAR',
    'SWAGGER_UI_FAVICON_HREF': 'SIDECAR',
    'REDOC_DIST': 'SIDECAR'
}

# Ckeditor Config
CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
    }
}

# Config CORS
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_METHODS = ["DELETE", "GET", "OPTIONS", "PATCH", "POST", "PUT", ]
# Application definition
CSRF_TRUSTED_ORIGINS = env('CSRF_TRUSTED_ORIGINS').split(',')

# Config CustomUser
if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
