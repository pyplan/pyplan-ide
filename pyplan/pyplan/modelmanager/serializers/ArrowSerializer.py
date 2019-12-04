from rest_framework import serializers

class ArrowsSerializer(serializers.Serializer):
    to = serializers.CharField(required=True, allow_blank=False, max_length=200)


# Workaround because "from" is a reserved word
ArrowsSerializer._declared_fields["from"] = serializers.CharField(
    required=True, allow_blank=False, max_length=200)
