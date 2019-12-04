from rest_framework import serializers


class InputTemplateDataChangeSerializer(serializers.Serializer):
    field = serializers.CharField()
    value = serializers.CharField(required=False, allow_blank=True)
    values = serializers.ListSerializer(child=serializers.CharField(), required=False)

class InputTemplateDataChangesSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    rowIndex = serializers.IntegerField(required=False)
    changes = InputTemplateDataChangeSerializer(many=True, default=[])


class InputTemplateSetDataParamsSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    rows = InputTemplateDataChangesSerializer(many=True, default=[])
    toDelete = serializers.ListSerializer(child=serializers.IntegerField(), required=False)


class OutputTemplateSetDataParamsSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    newId = serializers.IntegerField()
    err = serializers.CharField(required=False)
    rowIndex = serializers.IntegerField()
