from rest_framework import serializers

from pyplan.pyplan.modelmanager.classes.importModuleMap import ImportModuleMap

class ImportModuleMapItemSerializer(serializers.Serializer):
    currentId = serializers.CharField(required=True, allow_blank=False)
    currentIdChanged = serializers.CharField(required=True, allow_blank=False)
    newId = serializers.CharField(required=True, allow_blank=False)
    newIdChanged = serializers.CharField(required=True, allow_blank=False)
    currentName = serializers.CharField(required=True, allow_blank=False)
    newName = serializers.CharField(required=True, allow_blank=False)

    def create(self, validated_data):
        return ImportModuleMap(**validated_data)
