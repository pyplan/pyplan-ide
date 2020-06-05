from rest_framework import serializers

from ..classes.pivot import PivotQuery, PivotNodeValueChanges

# Request
class PivotQueryFilterSerializer(serializers.Serializer):
    field = serializers.CharField()
    values = serializers.ListField(child=serializers.CharField(), default=[])
    level = serializers.CharField(default=None)

class PivotQueryPositionFilterSerializer(serializers.Serializer):
    field = serializers.CharField()
    values = serializers.CharField(allow_blank=True)

class PivotQuerySerializer(serializers.Serializer):
    cube = serializers.CharField()
    columns = serializers.ListField(child=serializers.CharField(), default=[])
    hierarchicalColumns = serializers.ListField(child=serializers.CharField(), default=[])
    filters = PivotQueryFilterSerializer(many=True, default=[])
    positionFilters = PivotQueryPositionFilterSerializer(many=True, default=[])
    aggregator = serializers.CharField(default=None)
    measure = serializers.CharField(default=None)
    measures = serializers.ListField(child=serializers.CharField(), default=[])
    limit = serializers.IntegerField(default=None)
    mode = serializers.CharField(default=None)
    validationNode = serializers.CharField(default=None)
    excludeEmptyValues = serializers.BooleanField(default=True)
    text = serializers.CharField(default=None)
    resultType = serializers.CharField(required=False, allow_blank=True, allow_null=True)

    def create(self, validated_data):
        return PivotQuery(**validated_data)

class PivotNodeChangesSerializer(serializers.Serializer):
    filterList = serializers.ListField(child=serializers.DictField(
        child=serializers.CharField(trim_whitespace=False)))
    definition = serializers.CharField(allow_blank=True)

class PivotNodeValueChangesSerializer(serializers.Serializer):
    node = serializers.CharField()
    changes = PivotNodeChangesSerializer(many=True, default=[])

    def create(self, validated_data):
        return PivotNodeValueChanges(**validated_data)

# Response

class SubPivotItemSerializer(serializers.Serializer):
    field = serializers.CharField(default=None)
    name = serializers.CharField(default=None)
    numberFormat = serializers.CharField(default=None)

class PivotItemSerializer(serializers.Serializer):
    field = serializers.CharField(default=None)
    name = serializers.CharField(default=None)
    numberFormat = serializers.CharField(default=None)
    levels = SubPivotItemSerializer(many=True, default=[])

class PivotMetadataSerializer(serializers.Serializer):
    dims = PivotItemSerializer(many=True, default=[])
    measures = PivotItemSerializer(many=True, default=[])
    aggregator = serializers.CharField(default="sum")
    isEditable = serializers.BooleanField(default=None)
    nodeProperties = serializers.DictField(default=None)
