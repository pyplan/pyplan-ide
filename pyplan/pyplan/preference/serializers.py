from rest_framework import serializers

from .models import Preference


class PreferenceSerializer(serializers.ModelSerializer):
    definition = serializers.JSONField(required=False)

    class Meta:
        model = Preference
        fields = '__all__'
