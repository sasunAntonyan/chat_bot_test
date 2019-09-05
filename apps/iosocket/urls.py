from django.conf.urls import url

from apps.iosocket.views import index

urlpatterns = [
    url(r'', index, name='index'),
]