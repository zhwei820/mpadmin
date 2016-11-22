# coding=utf-8
from django.conf.urls import url
from django.contrib import admin

from item.views import ItemCategoryCreateAPIView, ItemCategoryUpdateAPIView,\
    ItemCategoryRetrieveDestroyAPIView, ItemUpdateAPIView, ItemCreateAPIView, ItemRetrieveDestroyAPIView, \
    ItemCategoryListAPIView, ItemWithCategoryIDListAPIView, ItemCategoryWithGroupIDListAPIView

urlpatterns = [
    url(r'^category/create/$', ItemCategoryCreateAPIView.as_view()),
    url(r'^category/(?P<id>\w{24})/update/$', ItemCategoryUpdateAPIView.as_view()),
    url(r'^category/(?P<id>\w{24})/$', ItemCategoryRetrieveDestroyAPIView.as_view()),
    url(r'^category/list/$', ItemCategoryListAPIView.as_view()),
    url(r'^category/(?P<id>\w{24})/list/$', ItemCategoryWithGroupIDListAPIView.as_view()),
    url(r'^item/create/$', ItemCreateAPIView.as_view()),
    url(r'^item/(?P<id>\w{24})/update/$', ItemUpdateAPIView.as_view()),
    url(r'^item/(?P<id>\w{24})/$', ItemRetrieveDestroyAPIView.as_view()),
    url(r'^item/(?P<id>\w{24})/list/$', ItemWithCategoryIDListAPIView.as_view()),
]
