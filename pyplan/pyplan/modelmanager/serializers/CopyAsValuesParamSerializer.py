from rest_framework import serializers

from pyplan.pyplan.modelmanager.classes.copyAsValuesParam import CopyAsValuesParam

class CopyAsValuesParamSerializer(serializers.Serializer):
    nodeId = serializers.CharField(required=True, allow_blank=False)
    asNewNode = serializers.BooleanField(required=True)

    def create(self,validated_data):
        return CopyAsValuesParam(**validated_data)
