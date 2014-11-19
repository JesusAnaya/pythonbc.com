from __future__ import unicode_literals
import os
from .settings import *

DEBUG = False

SECRET_KEY = os.environ["SECRET_KEY"]
NEVERCACHE_KEY = os.environ["TWITTER_APP_KEY"]

# Twitter app config
TWITTER_APP_KEY = os.environ["TWITTER_APP_KEY"]
TWITTER_APP_SECRET = os.environ["TWITTER_APP_SECRET"]

# Data base config
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.environ["PYTHONBC_DB_NAME"],
        "USER": os.environ["PYTHONBC_DB_USER"],
        "PASSWORD": os.environ["PYTHONBC_DB_PASS"],
        "HOST": "localhost",
        "PORT": "3306",
    }
}

CACHE_MIDDLEWARE_KEY_PREFIX = "pythonbc"
CACHE_MIDDLEWARE_SECONDS = 600

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.memcached.MemcachedCache",
        "LOCATION": "127.0.0.1:11211",
    }
}

RAVEN_CONFIG = {
    'dsn': 'https://{0}@app.getsentry.com/22752'.format(os.environ['RAVEN_ID']),
}

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTOCOL", "https")

ALLOWED_HOSTS = ('pythonbc.co', 'pythonbc.com')

EMAIL_USE_TLS = True
EMAIL_HOST = os.environ["EMAIL_HOST"]
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ["EMAIL_HOST_USER"]
EMAIL_HOST_PASSWORD = os.environ["EMAIL_HOST_PASSWORD"]
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


####################
# DYNAMIC SETTINGS #
####################

# set_dynamic_settings() will rewrite globals based on what has been
# defined so far, in order to provide some better defaults where
# applicable. We also allow this settings module to be imported
# without Mezzanine installed, as the case may be when using the
# fabfile, where setting the dynamic settings below isn't strictly
# required.
try:
    from mezzanine.utils.conf import set_dynamic_settings
except ImportError:
    pass
else:
    set_dynamic_settings(globals())

