# coding=utf-8
import datetime

from arch.models import Layer, Group
from arch.serializers import LayerSerializer, GroupSerializer
from django.shortcuts import render


# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_mongoengine.generics import CreateAPIView, UpdateAPIView, RetrieveDestroyAPIView


class LayerCreateAPIView(CreateAPIView):
    serializer_class = LayerSerializer
    permission_classes = (IsAuthenticated,)


class LayerUpdateAPIView(UpdateAPIView):
    serializer_class = LayerSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        obj_id = self.kwargs.get("id")
        return Layer.objects(id=obj_id).first()

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        if instance:
            instance.utime = datetime.datetime.now()
        return Response(serializer.data)


class LayerRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    serializer_class = LayerSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        obj_id = self.kwargs.get("id")
        return Layer.objects(id=obj_id).first()


class GroupCreateAPIView(CreateAPIView):
    serializer_class = GroupSerializer
    permission_classes = (IsAuthenticated,)


class GroupUpdateAPIView(UpdateAPIView):
    serializer_class = GroupSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        obj_id = self.kwargs.get("id")
        return Group.objects(id=obj_id).first()

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        if instance:
            instance.utime = datetime.datetime.now()
        return Response(serializer.data)


class GroupRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    serializer_class = GroupSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        obj_id = self.kwargs.get("id")
        return Group.objects(id=obj_id).first()
