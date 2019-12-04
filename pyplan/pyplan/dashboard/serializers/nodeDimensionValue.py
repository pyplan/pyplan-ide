from rest_framework import serializers


class NodeDimensionValueSerializer(serializers.Serializer):
    type = serializers.CharField(default="", allow_blank=True, allow_null=True)
    value = serializers.CharField(default="")
    selected = serializers.BooleanField(default=False)
    geoDef = serializers.CharField(default=None, allow_null=True)
