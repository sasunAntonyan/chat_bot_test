from django.conf.urls import url
from rest_framework import routers

from apps.chat_bot.views import ChatBotApiView, ThreadViewSet

router = routers.DefaultRouter()
router.register(r'threads', ThreadViewSet, base_name='threads')

urlpatterns = [
    url(r'chat-bot/', ChatBotApiView.as_view(), name='chat_bot'),

]
