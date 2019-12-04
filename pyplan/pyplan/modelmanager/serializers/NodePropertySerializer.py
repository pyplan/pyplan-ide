from rest_framework import serializers

class NodePropertySerializer(serializers.Serializer):
    name = serializers.CharField(required=True, allow_blank=False, max_length=200)
    value = serializers.CharField(required=False, allow_blank=True, allow_null=True, default="")
