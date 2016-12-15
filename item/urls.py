# coding=utf-8
from django.conf.urls import url
from django.contrib import admin

from item.views import ItemCategoryListCreateAPIView,\
    ItemCategoryRetrieveUpdateDestroyAPIView, ItemListCreateAPIView, ItemRetrieveUpdateDestroyAPIView, \
    ItemWithCategoryIDListAPIView, ItemCategoryWithGroupIDListAPIView

urlpatterns = [
]
