from rest_framework import serializers

from pyplan.pyplan.modelmanager.classes.modelInfo import ModelInfo


class ModelInfoSerializer(serializers.Serializer):
    modelId = serializers.CharField(allow_blank=True)
    name = serializers.CharField(allow_blank=True, allow_null=True)
    new_session_key = serializers.CharField(allow_blank=True)
    uri = serializers.CharField(allow_blank=True)
    daysToExpire = serializers.CharField(allow_blank=True)
    readonly = serializers.BooleanField(default=False)
    readOnlyReason = serializers.CharField(allow_blank=True)
    engineURI = serializers.CharField(allow_blank=True)
    engineUID = serializers.CharField(allow_blank=True)
    engineParams = serializers.CharField(allow_blank=True)
    nodeIdInBackground = serializers.CharField(required=False, allow_blank=True)
    onOpenModel = serializers.CharField(allow_blank=True, allow_null=True)
    onOpenDashId = serializers.CharField(required=False, allow_blank=True, allow_null=True)

    def create(self, validated_data):
        instance = ModelInfo()
        instance.modelId = validated_data.get("modelId", instance.modelId)
        instance.name = validated_data.get("name", instance.name)
        instance.new_session_key = validated_data.get("new_session_key", instance.new_session_key)
        instance.uri = validated_data.get("uri", instance.uri)
        instance.daysToExpire = validated_data.get("daysToExpire", instance.daysToExpire)
        instance.readonly = validated_data.get("readonly", instance.readonly)
        instance.readOnlyReason = validated_data.get("readOnlyReason", instance.readOnlyReason)
        instance.engineURI = validated_data.get("engineURI", instance.engineURI)
        instance.engineUID = validated_data.get("engineUID", instance.engineUID)
        instance.engineParams = validated_data.get("engineParams", instance.engineParams)
        instance.nodeIdInBackground = validated_data.get("nodeIdInBackground", instance.nodeIdInBackground)
        instance.onOpenModel = validated_data.get("onOpenModel", instance.onOpenModel)
        instance.onOpenDashId = validated_data.get("onOpenDashId", instance.onOpenDashId)

        return instance
