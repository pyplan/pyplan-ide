from rest_framework import serializers

class SendPasswordResetEmailSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    publicUrl = serializers.CharField(required=True)
