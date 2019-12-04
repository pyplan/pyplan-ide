from rest_framework import serializers

from pyplan.pyplan.modelmanager.classes.exportModuleToFile import ExportModuleToFile

class ExportModuleToFileSerializer(serializers.Serializer):
    moduleId = serializers.CharField(required=True, allow_blank=False)
    exportType = serializers.CharField(required=True, allow_blank=False)

    def create(self, validated_data):
        return ExportModuleToFile(**validated_data)
