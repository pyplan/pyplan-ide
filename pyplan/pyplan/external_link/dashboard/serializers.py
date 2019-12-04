from rest_framework import serializers

from pyplan.pyplan.external_link.serializers import ExternalLinkSerializer

from .models import DashboardExternalLink


class DashboardExternalLinkSerializer(ExternalLinkSerializer):

    class Meta:
        model = DashboardExternalLink
        fields = '__all__'
