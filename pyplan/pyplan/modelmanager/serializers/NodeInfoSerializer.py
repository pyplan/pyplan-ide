from rest_framework import serializers

from pyplan.pyplan.modelmanager.classes.modelInfo import ModelInfo

class NodeInfoSerializer(serializers.Serializer):
    fill = serializers.CharField(required=False, allow_blank=True, max_length=200)
    showBorder = serializers.CharField(required=False, allow_blank=True, max_length=200)
    showInputs = serializers.CharField(required=False, allow_blank=True, max_length=200)
    showLabel = serializers.CharField(required=False, allow_blank=True, max_length=200)
    showOutputs = serializers.CharField(required=False, allow_blank=True, max_length=200)
    useNodeFont = serializers.CharField(required=False, allow_blank=True, max_length=200)
    formWidth = serializers.CharField(required=False, allow_blank=True, max_length=200)
    showBevel = serializers.CharField(required=False, allow_blank=True, max_length=200)
    showFormIcon = serializers.CharField(required=False, allow_blank=True, max_length=200)
    version = serializers.CharField(required=False, allow_blank=True, max_length=200)

    def create(self, validated_data):
        return(ModelInfo(**validated_data))
