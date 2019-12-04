from rest_framework import serializers

from .models import PreferenceModule


class PreferenceModuleSerializer(serializers.ModelSerializer):

    class Meta:
        model = PreferenceModule
        fields = '__all__'
