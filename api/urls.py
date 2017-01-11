# coding=utf-8
from django.conf.urls import url
from django.contrib import admin

from arch.views import LayerListCreateAPIView, LayerRetrieveUpdateDestroyAPIView, \
    GroupListCreateAPIView, GroupRetrieveUpdateDestroyAPIView,\
    GroupWithLayerIDListAPIView

from item.views import ItemCategoryListCreateAPIView,\
    ItemCategoryRetrieveUpdateDestroyAPIView, ItemListCreateAPIView, ItemRetrieveUpdateDestroyAPIView, \
    ItemWithCategoryIDListAPIView, ItemCategoryWithGroupIDListAPIView

urlpatterns = [
    url(r'^layers/$', LayerListCreateAPIView.as_view()),
    url(r'^layers/(?P<id>\w{24})/$', LayerRetrieveUpdateDestroyAPIView.as_view()),
    url(r'^groups/$', GroupListCreateAPIView.as_view()),
    url(r'^groups/(?P<id>\w{24})/$', GroupRetrieveUpdateDestroyAPIView.as_view()),
    url(r'^layers/(?P<id>\w{24})/groups/$', GroupWithLayerIDListAPIView.as_view()),
]

urlpatterns += [
    url(r'^categories/$', ItemCategoryListCreateAPIView.as_view()),
    url(r'^categories/(?P<id>\w{24})/$', ItemCategoryRetrieveUpdateDestroyAPIView.as_view()),
    url(r'^groups/(?P<id>\w{24})/categories/$', ItemCategoryWithGroupIDListAPIView.as_view()),
    url(r'^items/$', ItemListCreateAPIView.as_view()),
    url(r'^items/(?P<id>\w{24})/$', ItemRetrieveUpdateDestroyAPIView.as_view()),
    url(r'^categories/(?P<id>\w{24})/items/$', ItemWithCategoryIDListAPIView.as_view()),
]
