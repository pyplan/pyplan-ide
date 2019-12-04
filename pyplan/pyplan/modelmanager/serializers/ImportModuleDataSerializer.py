from rest_framework import serializers

from pyplan.pyplan.modelmanager.serializers.ImportModuleMapItemSerializer import ImportModuleMapItemSerializer
from pyplan.pyplan.modelmanager.classes.importModuleData import ImportModuleData

class ImportModuleDataSerializer(serializers.Serializer):
    parentModelId = serializers.CharField(required=True, allow_blank=False)
    importType = serializers.IntegerField(required=True)
    moduleFile = serializers.CharField(required=True, allow_blank=False)
    mapData = ImportModuleMapItemSerializer(many=True, default=[])
    fromTemp = serializers.BooleanField(default=True)
    currentModelPath = serializers.CharField(default="")

    def create(self, validated_data):
        return ImportModuleData(**validated_data)
