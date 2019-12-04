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
    timeFormat = serializers.CharField(default="A")
    timeFormatType = serializers.CharField(default="FLO")
    calendarType = serializers.CharField(default="CAL")

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
        instance.timeFormat = validated_data.get('timeFormat', instance.timeFormat)
        instance.timeFormatType = validated_data.get('timeFormatType', instance.timeFormatType)
        instance.calendarType = validated_data.get('calendarType', instance.calendarType)
        return instance
