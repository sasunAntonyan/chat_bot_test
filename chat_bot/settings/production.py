from django.conf import settings

settings.configure()
from chat_bot.settings.base import *

DEBUG = True
THUMBNAIL_DEBUG = True

ALLOWED_HOSTS = ['*', ]

INSTALLED_APPS = INSTALLED_APPS + THIRD_PARTY_APPS + PROJECT_APPS
