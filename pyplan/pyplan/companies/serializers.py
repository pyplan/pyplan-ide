from rest_framework import serializers

from .models import Company


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ('id', 'code', 'name', 'system', 'active', 'licence')
        read_only_fields = ('code', )

class FullCompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ('id', 'code', 'name', 'system', 'active', 'departments',)
        depth = 1
        read_only_fields = ('code', )

class LightCompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ('id', 'code', 'name',)

class CreateCompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ('code', 'name', 'system', 'active', 'licence')


class UpdateCompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ('id', 'code', 'name', 'system', 'active', 'licence')
