from config.settings import *

DEBUG = True
TEMPLATE_DEBUG = True

# Data base config
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "testdb.db"
    }
}
