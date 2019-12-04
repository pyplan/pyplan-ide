from rest_framework import serializers


class InputTemplateSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    code = serializers.CharField(required=True)
    name = serializers.CharField(required=True)
    definition = serializers.JSONField(required=False)
    filepath = serializers.CharField(required=False)
    owner = serializers.IntegerField(source="owner.id", required=False)


class InputTemplateListSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    code = serializers.CharField(required=True)
    filepath = serializers.CharField(required=False)
    name = serializers.CharField(required=True)

class InputTemplateGetDataFilterSerializer(serializers.Serializer):
    field = serializers.CharField(required=False)
    values = serializers.ListSerializer(child=serializers.CharField())
    useLike = serializers.BooleanField(default=False)
    relatedManyToManyKey = serializers.CharField(required=False)

class InputTemplateGetDataSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    code = serializers.CharField(required=False)
    fromReg = serializers.IntegerField(default=0)
    toReg = serializers.IntegerField(default=0)
    sortBy = serializers.CharField(required=False)
    includeHistory = serializers.BooleanField(default=False)
    filters = InputTemplateGetDataFilterSerializer(many=True, default=[])
