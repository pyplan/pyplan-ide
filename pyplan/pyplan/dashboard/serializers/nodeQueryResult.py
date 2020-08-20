from rest_framework import serializers

from ..classes.nodeQueryResult import NodeQueryResult
from .nodeDimension import NodeDimensionSerializer

class NodeQueryResultSerializer(serializers.Serializer):
    node = serializers.CharField(required=False)
    dims = NodeDimensionSerializer(many=True, default=[])
    rows = NodeDimensionSerializer(many=True, default=[])
    columns = NodeDimensionSerializer(many=True, default=[])
    summaryBy = serializers.CharField(default="sum")
    fromRow = serializers.IntegerField(required=False)
    toRow = serializers.IntegerField(required=False)
    bottomTotal = serializers.BooleanField(default=False)
    rightTotal = serializers.BooleanField(default=False)
    hideEmpty = serializers.CharField(default=None, required=False)

    def create(self, validated_data):
        return NodeQueryResult(**validated_data)

    def update(self, instance, validated_data):
        instance.node = validated_data.get('node', instance.node)
        instance.dims = validated_data.get('dims', instance.dims)
        instance.rows = validated_data.get('rows', instance.rows)
        instance.columns = validated_data.get('columns', instance.columns)
        instance.summaryBy = validated_data.get('summaryBy', instance.summaryBy)
        instance.fromRow = validated_data.get('fromRow', instance.fromRow)
        instance.toRow = validated_data.get('toRow', instance.toRow)
        instance.bottomTotal = validated_data.get('bottomTotal', instance.bottomTotal)
        instance.rightTotal = validated_data.get('rightTotal', instance.rightTotal)
        instance.hideEmpty = validated_data.get('hideEmpty', instance.hideEmpty)

        return instance
