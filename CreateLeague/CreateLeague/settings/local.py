from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# SET YOUR DATABASE DATA
DATABASES = {
      'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': "localhost",
        "PORT": "3306",
        "USER": "root",
        "PASSWORD": "",
        "NAME": "ligas",
        "OPTIONS": {
            "init_command": "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}

STATIC_URL = 'static/'