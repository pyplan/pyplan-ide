from rest_framework import serializers

from ..classes.nodeDimension import NodeDimension
from .nodeDimensionValue import NodeDimensionValueSerializer
from pyplan.pyplan.common.serializers.RecursiveField import RecursiveField


class NodeDimensionSerializer(serializers.Serializer):
    field = serializers.CharField(required=True)
    name = serializers.CharField(default="")
    description = serializers.CharField(allow_blank=True, allow_null=True)
    values = NodeDimensionValueSerializer(many=True, default=[])
    isTime = serializers.BooleanField(default=False)
    isGeo = serializers.BooleanField(default=False)
    numberFormat = serializers.CharField(default=None, allow_null=True)
    levels = RecursiveField(many=True, default=[])
    currentLevel = serializers.CharField(default=None, allow_null=True)

    def create(self, validated_data):
        return NodeDimension(**validated_data)

    def update(self, instance, validated_data):
        instance.field = validated_data.get('field', instance.field)
        return instance
