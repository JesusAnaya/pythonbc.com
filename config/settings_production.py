from __future__ import unicode_literals
import os
from config.settings import *

DEBUG = False

SECRET_KEY = os.environ["SECRET_KEY"]
NEVERCACHE_KEY = os.environ["NEVERCACHE_KEY"]

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

CACHE_MIDDLEWARE_KEY_PREFIX = os.environ['CACHE_PREFIX']
CACHE_MIDDLEWARE_SECONDS = 600

SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'

CACHES = {
    'default': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': '127.0.0.1:6379',
        'OPTIONS': {
            'DB': 1,
            'PASSWORD': os.environ["REDIS_PASSWORD"]
        },
    },
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
