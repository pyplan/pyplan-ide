from rest_framework import serializers

from pyplan.pyplan.external_link.serializers import ExternalLinkSerializer

from .models import ReportExternalLink


class ReportExternalLinkSerializer(ExternalLinkSerializer):

    class Meta:
        model = ReportExternalLink
        fields = '__all__'
