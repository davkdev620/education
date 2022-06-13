"""This is the settings file used by your live production server(s).
That is, the server(s) that host the real live website.
This file contains production-level settings only. It is sometimes called prod.py."""

from .base import *

DEBUG = False

ADMINS = (
    ('YOUR_NAME', 'Youremail@gmail.com'),
)

ALLOWED_HOSTS = ['education.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'education',
        'USER': 'education',
        'PASSWORD': '*****',
    }
}

# Email settings.
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'Yourmail@gmail.com'
EMAIL_HOST_PASSWORD = '******'
EMAIL_PORT = '587'
EMAIL_USE_TLS = True

# SSL config
SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True
