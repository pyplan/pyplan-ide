from django.contrib.auth.models import ContentType, Permission
from rest_framework import serializers


class ContentTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContentType
        fields = '__all__'

class PermissionSerializer(serializers.ModelSerializer):
    content_type = ContentTypeSerializer()

    class Meta:
        model = Permission
        fields = ('id', 'name', 'content_type', 'codename')
