"""This is the settings file for working on the project locally.
Local development-specific settings include:
DEBUG mode, log level, and activation of
developer tools like django-debug-toolbar."""

from .base import *

DEBUG = True

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
	}
}

# Email settings.
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Debug toolbar.
INSTALLED_APPS += ['debug_toolbar', ]

