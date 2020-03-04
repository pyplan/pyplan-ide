import os
from distutils.util import strtobool
from os.path import join

import environ
from configurations import Configuration
from corsheaders.defaults import default_headers

root = environ.Path(__file__) - 3
BASE_DIR = root()

# set default values and casting
env = environ.Env()


class Common(Configuration):

    INSTALLED_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.sites',
        'whitenoise.runserver_nostatic',
        'django.contrib.staticfiles',

        # Third party apps
        'rest_framework',            # utilities for rest apis
        'rest_framework.authtoken',  # token authentication
        'django_filters',            # for filtering rest endpoints
        'corsheaders',               # adds CORS headers to responses
        'channels',                  # websockets

        # Your apps
        'pyplan.pyplan.PyplanAppConfig',
    )

    # Channels
    ASGI_APPLICATION = 'pyplan.config.urls.application'
    CHANNEL_LAYERS = {
        'default': {
            'BACKEND': 'channels.layers.InMemoryChannelLayer',
        },
    }

    SITE_ID = 1

    # https://docs.djangoproject.com/en/2.0/topics/http/middleware/
    MIDDLEWARE = (
        'corsheaders.middleware.CorsMiddleware',
        'django.middleware.security.SecurityMiddleware',
        'whitenoise.middleware.WhiteNoiseMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        # Custom
        'pyplan.pyplan.common.middlewares.sessionMiddleware.SessionMiddleware',
        'pyplan.pyplan.common.middlewares.exceptionMiddleware.ExceptionMiddleware',
    )

    ALLOWED_HOSTS = ['*']
    ROOT_URLCONF = 'pyplan.config.urls'
    SECRET_KEY = env.str('DJANGO_SECRET_KEY')
    WSGI_APPLICATION = 'pyplan.config.wsgi.application'

    # CORS
    CORS_ORIGIN_ALLOW_ALL = True
    # CORS_ORIGIN_WHITELIST = (
    #     'google.com',
    #     'hostname.example.com',
    #     'localhost:9000',
    #     '127.0.0.1:9000'
    # )
    CORS_ALLOW_HEADERS = default_headers + (
        'session-key',
    )
    CORS_EXPOSE_HEADERS = (
        'Content-Disposition',
    )

    # Email
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

    ADMINS = (
        ('Author', 'info@pyplan.com'),
    )

    # General
    APPEND_SLASH = False
    TIME_ZONE = 'UTC'
    LANGUAGE_CODE = 'en-us'
    # If you set this to False, Django will make some optimizations so as not
    # to load the internationalization machinery.
    USE_I18N = False
    USE_L10N = True
    USE_TZ = True
    LOGIN_REDIRECT_URL = '/'
    SESSION_COOKIE_AGE = env.int('SESSION_TIMEOUT', default=60 * 5)
    GUEST_SESSION_TIMEOUT = env.int('GUEST_SESSION_TIMEOUT', default=60 * 5)
    TIMEOUT_FOR_PROCESSING_IN_HOURS = env.int(
        'TIMEOUT_FOR_PROCESSING_IN_HOURS', default=4) * 60 * 60

    BACKEND_DIR = BASE_DIR

    FRONTEND_DIR = os.path.abspath(os.path.join(BACKEND_DIR, 'frontend'))

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/2.0/howto/static-files/

    STATIC_ROOT = os.path.normpath(join(BASE_DIR, 'static'))

    EMAIL_TEMPLATES = os.path.normpath(
        join(BASE_DIR, 'pyplan', 'common', 'email', 'templates'))

    STATICFILES_DIRS = [EMAIL_TEMPLATES, FRONTEND_DIR]

    STATIC_URL = '/static/'
    STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    )

    STATICFILES_STORAGE = (
        'whitenoise.storage.CompressedManifestStaticFilesStorage')
    WHITENOISE_ROOT = os.path.join(FRONTEND_DIR)

    # Media files
    # TODO: tomar paths de documents y temps ??
    MEDIA_ROOT = os.getenv("DATA_PATH") if os.getenv(
        "DATA_PATH") else os.path.join(os.path.expanduser('~'), 'pyplan')
    TMP_ROOT = "/tmp"

    MEDIA_URL = '/media/'

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': STATICFILES_DIRS,
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

    # Set DEBUG to False as a default for safety
    # https://docs.djangoproject.com/en/dev/ref/settings/#debug
    DEBUG = env.bool('DJANGO_DEBUG', default=False)

    AUTHENTICATION_BACKENDS = (
        # Needed to login by username in Django admin, regardless of `allauth`
        'django.contrib.auth.backends.ModelBackend',
    )

    # Password Validation
    # https://docs.djangoproject.com/en/2.0/topics/auth/passwords/#module-django.contrib.auth.password_validation
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

    # Logging
    LOGGING = {}

    # Custom user app
    AUTH_USER_MODEL = 'pyplan.User'

    # token expiration
    TOKEN_EXPIRED_AFTER_SECONDS = 3600

    # Django Rest Framework
    REST_FRAMEWORK = {
        'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
        'PAGE_SIZE': env.int('DJANGO_PAGINATION_LIMIT', default=10),
        'DATETIME_FORMAT': '%Y-%m-%dT%H:%M:%S%z',
        'DEFAULT_RENDERER_CLASSES': (
            'rest_framework.renderers.JSONRenderer',
            'rest_framework.renderers.BrowsableAPIRenderer',
        ),
        'DEFAULT_PERMISSION_CLASSES': [
            'rest_framework.permissions.IsAuthenticated',
        ],
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework.authentication.TokenAuthentication',
            'rest_framework.authentication.SessionAuthentication',
        ),
        # CoreAPI deprecation https://www.django-rest-framework.org/community/3.10-announcement/
        'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
    }
