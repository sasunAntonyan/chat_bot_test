"""chat_bot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from django.views.static import serve
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions, routers

from apps.chat_bot.urls import router as chat_bot

schema_view = get_schema_view(
    openapi.Info(
        title="Chat Bot API",
        default_version='v1',
        description="For Huri",
        terms_of_service="https://www.betconstruct.com/",
        contact=openapi.Contact(email="sasun.antonyan.31@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    # validators=['flex', 'ssv'],
    public=True,
    permission_classes=(permissions.AllowAny,),
)


class DefaultRouter(routers.DefaultRouter):
    def extend(self, app_router):
        self.registry.extend(app_router.registry)


router = DefaultRouter()
router.extend(chat_bot)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api/$', schema_view.with_ui('swagger', cache_timeout=None), name='schema-swagger-ui'),
    path('redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    url('', include(('apps.chat_bot.urls', 'chat_bot'), namespace='chat_bot')),
    path('chat/', include('apps.iosocket.urls')),
]

urlpatterns += [
    url(r'^static/(?P<path>.*)$', serve, {
        'document_root': settings.STATIC_ROOT,
    }),
]
