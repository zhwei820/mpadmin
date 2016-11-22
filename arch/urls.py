# coding=utf-8
from django.conf.urls import url
from django.contrib import admin

from arch.views import LayerCreateAPIView, LayerUpdateAPIView, LayerRetrieveDestroyAPIView,\
    GroupCreateAPIView, GroupUpdateAPIView, GroupRetrieveDestroyAPIView, LayerListAPIView,\
    GroupWithLayerIDListAPIView

urlpatterns = [
    url(r'^layer/create/$', LayerCreateAPIView.as_view()),
    url(r'^layer/(?P<id>\w{24})/update/$', LayerUpdateAPIView.as_view()),
    url(r'^layer/list/$', LayerListAPIView.as_view()),
    url(r'^layer/(?P<id>\w{24})/$', LayerRetrieveDestroyAPIView.as_view()),
    url(r'^group/create/$', GroupCreateAPIView.as_view()),
    url(r'^group/(?P<id>\w{24})/update/$', GroupUpdateAPIView.as_view()),
    url(r'^group/(?P<id>\w{24})/', GroupRetrieveDestroyAPIView.as_view()),
    url(r'^group/(?P<id>\w{24})/list/$', GroupWithLayerIDListAPIView.as_view()),
]