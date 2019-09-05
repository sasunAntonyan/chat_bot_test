"""
WSGI config for chat_bot project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
from socketio import WSGIApp

from django.core.wsgi import get_wsgi_application

from apps.iosocket.views import sio

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chat_bot.settings.production")

django_app = get_wsgi_application()
application = WSGIApp(sio, django_app)
