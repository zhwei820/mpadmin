# coding=utf-8
from django.conf.urls import url
from django.contrib import admin

from arch.views import LayerListCreateAPIView, LayerRetrieveUpdateDestroyAPIView, \
    GroupListCreateAPIView, GroupRetrieveUpdateDestroyAPIView,\
    GroupWithLayerIDListAPIView

urlpatterns = [
    url(r'^layers/$', LayerListCreateAPIView.as_view()),
    url(r'^layers/(?P<id>\w{24})/$', LayerRetrieveUpdateDestroyAPIView.as_view()),
    url(r'^groups/$', GroupListCreateAPIView.as_view()),
    url(r'^groups/(?P<id>\w{24})/$', GroupRetrieveUpdateDestroyAPIView.as_view()),
    url(r'^layers/(?P<id>\w{24})/groups/$', GroupWithLayerIDListAPIView.as_view()),
]
