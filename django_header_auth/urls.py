from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from rest_framework import urls as rest_framework_urls

from .views import ConsumerViewSet


urlpatterns = [
    url(r'^$', ConsumerViewSet.as_view({'get': 'list', 'post': 'create'}), name="consumer-list"),
    url(r'^(?P<uuid>\w+)/$', ConsumerViewSet.as_view({'get': 'retrieve', 'delete': 'destroy'}), name="consumer-detail"),
]
