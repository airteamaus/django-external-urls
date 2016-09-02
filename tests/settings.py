""" Settings for tests. """

import tempfile

TMPDIR = tempfile.mkdtemp()

ROOT_URLCONF = 'tests.urls'

SECRET_KEY = 'ItIsSecret'

DEBUG = False

ALLOWED_HOSTS = ['testserver']

MEDIA_ROOT = TMPDIR

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

INSTALLED_APPS = (
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'external_urls',
    'tests',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
    },
]
