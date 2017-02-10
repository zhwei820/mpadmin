# coding=utf-8
from rest_framework_mongoengine.serializers import DocumentSerializer

from storage.models import StorageGroup # ,StorageLayer

class StorageGroupSerializer(DocumentSerializer):
    class Meta:
        model = StorageGroup
        exclude = ('ctime', 'utime')
