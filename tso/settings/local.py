from .common import *

ALLOWED_HOSTS = ['*']
DEBUG = True
if DEBUG:
    INSTALLED_APPS += ['silk']
    MIDDLEWARE += ['silk.middleware.SilkyMiddleware']