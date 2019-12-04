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
        instance = ModelPreference()
        instance.modelId = validated_data.get("modelId", instance.modelId)
        instance.changeIdentifier = validated_data.get("changeIdentifier", instance.changeIdentifier)
        instance.askBeforeRename = validated_data.get("askBeforeRename", instance.askBeforeRename)

        instance.identifier = validated_data.get("identifier", instance.identifier)
        instance.title = validated_data.get("title", instance.title)
        instance.onOpenModel = validated_data.get("onOpenModel", instance.onOpenModel)
        instance.onOpenDashId = validated_data.get("onOpenDashId", instance.onOpenDashId)

        return instance

    def createBlank(self):
        instance = ModelPreference()
        return instance
