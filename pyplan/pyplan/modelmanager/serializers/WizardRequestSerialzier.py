from rest_framework import serializers

from pyplan.pyplan.modelmanager.classes.wizardRequest import WizardRequest

class WizardRequestSerializer(serializers.Serializer):
    action = serializers.CharField(required=True)
    wizard = serializers.CharField(required=True)

    def create(self, validated_data):
        return(WizardRequest(**validated_data))
