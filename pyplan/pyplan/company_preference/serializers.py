from rest_framework import serializers

from .models import CompanyPreference


class CompanyPreferenceSerializer(serializers.ModelSerializer):
    definition = serializers.JSONField(required=False)

    class Meta:
        model = CompanyPreference
        fields = '__all__'
