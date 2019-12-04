from rest_framework import serializers


class ObjectField(serializers.Field):
    def to_representation(self, value):
        return value
