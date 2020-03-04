from rest_framework import serializers

from pyplan.pyplan.modelmanager.classes.modelPreference import ModelPreference


class ModelPreferenceSerializer(serializers.Serializer):
    modelId = serializers.CharField(required=True)
    identifier = serializers.CharField(required=False, allow_null=True)
    title = serializers.CharField(required=False, allow_blank=True)
    changeIdentifier = serializers.CharField(required=True)
    askBeforeRename = serializers.CharField(required=False)
    onOpenModel = serializers.CharField(required=False, allow_blank=True)
    onOpenDashId = serializers.CharField(required=False, allow_blank=True, allow_null=True)

    def create(self, validated_data):
        return ModelPreference(**validated_data)

    def createBlank(self):
        instance = ModelPreference()
        return instance
