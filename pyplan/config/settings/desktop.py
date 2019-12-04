import os

import environ

from .common import Common

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

root = environ.Path(__file__) - 3
ROOT_DIR = root()


class Desktop(Common):
    # Testing
    INSTALLED_APPS = Common.INSTALLED_APPS
    INSTALLED_APPS += ('django_nose',)
    TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
    NOSE_ARGS = [
        BASE_DIR,
        '-s',
        '--nologcapture',
        '--with-coverage',
        '--with-progressive',
        '--cover-package=app'
    ]

    # Email
    EMAIL_HOST = 'localhost'
    EMAIL_PORT = 1025
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(ROOT_DIR, 'pyplan.db'),
        }
    }
