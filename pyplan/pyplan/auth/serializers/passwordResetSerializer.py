from rest_framework import serializers

class PasswordResetSerializer(serializers.Serializer):
    query = serializers.CharField(required=True)
