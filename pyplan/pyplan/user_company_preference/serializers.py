from rest_framework import serializers

from .models import UserCompanyPreference


class UserCompanyPreferenceSerializer(serializers.ModelSerializer):
    definition = serializers.JSONField(required=False)

    class Meta:
        model = UserCompanyPreference
        fields = '__all__'
