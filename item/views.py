# coding=utf-8
from django.shortcuts import render


# Create your views here.
from django.views.generic import View
import datetime

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_mongoengine.generics import CreateAPIView,\
    UpdateAPIView, RetrieveDestroyAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView

from item.models import ItemCategory, Item
from item.serializers import ItemCategorySerializer, ItemSerializer

from util.fields_validation import validate_category_structure, validate_item_structure


class ItemCategoryListCreateAPIView(ListCreateAPIView):
    serializer_class = ItemCategorySerializer
    permission_classes = (IsAuthenticated,)
    queryset = ItemCategory.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        state, reason = validate_category_structure(request.data)
        if state < 0:
            return Response(reason, status=status.HTTP_400_BAD_REQUEST)

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ItemCategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ItemCategorySerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        obj_id = self.kwargs.get("id")
        return ItemCategory.objects(id=obj_id).first()

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        if not instance:
            return Response({"msg": "object does not exist."}, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

        state, reason = validate_category_structure(request.data)
        if state < 0:
            return Response(reason, status=status.HTTP_400_BAD_REQUEST)

        self.perform_update(serializer)
        if instance:
            instance.utime = datetime.datetime.now()
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        # 当该CI对象模型未产生任何CI对象时，可以将其删除
        item_obj_set = Item.objects(category=instance)
        if item_obj_set:
            return Response({"msg": "can't delete this category because it has items reserved."},
                            status=status.HTTP_400_BAD_REQUEST)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if not instance:
            return Response({"msg": "object does not exist."}, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class ItemCategoryWithGroupIDListAPIView(ListAPIView):
    serializer_class = ItemCategorySerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        obj_id = self.kwargs.get("id")
        return ItemCategory.objects(group=obj_id)


class ItemListCreateAPIView(CreateAPIView):
    serializer_class = ItemSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Item.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        state, reason = validate_item_structure(request.data)
        if state < 0:
            return Response(reason, status=status.HTTP_400_BAD_REQUEST)

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ItemRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ItemSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        obj_id = self.kwargs.get("id")
        return Item.objects(id=obj_id).first()

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        if not instance:
            return Response({"msg": "object does not exist."}, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

        state, reason = validate_item_structure(request.data)
        if state < 0:
            return Response(reason, status=status.HTTP_400_BAD_REQUEST)

        self.perform_update(serializer)
        if instance:
            instance.utime = datetime.datetime.now()
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if not instance:
            return Response({"msg": "object does not exist."}, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


# 列举属于某个category的items
class ItemWithCategoryIDListAPIView(ListAPIView):
    serializer_class = ItemSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        obj_id = self.kwargs.get("id")
        return Item.objects(category=obj_id)
