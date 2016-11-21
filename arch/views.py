# coding=utf-8
import datetime

from rest_framework import status

from arch.models import Layer, Group
from arch.serializers import LayerSerializer, GroupSerializer
from django.shortcuts import render


# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_mongoengine.generics import CreateAPIView, UpdateAPIView, RetrieveDestroyAPIView, ListAPIView


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
        if not instance:
            return Response({"msg": "object does not exist."}, status=status.HTTP_400_BAD_REQUEST)
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

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if not instance:
            return Response({"msg": "object does not exist."}, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class LayerListAPIView(ListAPIView):
    queryset = Layer.objects.all()
    serializer_class = LayerSerializer
    pagination_class = None
    permission_classes = (IsAuthenticated,)


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
        if not instance:
            return Response({"msg": "object does not exist."}, status=status.HTTP_400_BAD_REQUEST)
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

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if not instance:
            return Response({"msg": "object does not exist."}, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class GroupWithLayerIDListAPIView(ListAPIView):
    serializer_class = GroupSerializer
    pagination_class = None
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        obj_id = self.kwargs.get("id")
        return Group.objects(layer=obj_id)
