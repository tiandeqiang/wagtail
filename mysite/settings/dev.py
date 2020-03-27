from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'n!0e87=hs^5tm#5egxma&fuhn965u)w0%@#v^37k0q36al*3j3'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*'] 

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


try:
    from .local import *
except ImportError:
    pass
