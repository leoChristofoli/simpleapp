from __future__ import absolute_import, unicode_literals

from .base import *

print('dev.settings')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-bwl#cl(-%4rrdn@x^b8wdr&m@n@n1ndacqx=hhz7_mz5ljj*6'


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


try:
    from .local import *
except ImportError:
    pass
