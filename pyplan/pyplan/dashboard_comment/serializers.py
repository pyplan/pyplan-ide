from rest_framework import serializers

from .models import DashboardComment


class DashboardCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = DashboardComment
        fields = '__all__'
