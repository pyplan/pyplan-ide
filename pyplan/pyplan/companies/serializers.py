from rest_framework import serializers
from .models import Company


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ('id', 'code', 'name', 'system', 'active', 'licence')
        read_only_fields = ('code', )


class CreateCompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ('code', 'name', 'system', 'active', 'licence')


class UpdateCompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ('id', 'code', 'name', 'system', 'active', 'licence')

# cant import any serializers from department serializers due to circular references with the company serializer


class FakeDepartmentSerializer(serializers.Serializer):
    id = serializers.CharField(required=True)
    code = serializers.CharField(max_length=50, required=True)
    name = serializers.CharField(max_length=255, required=True)
    engine_definitions = serializers.JSONField(required=False, default={})
    login_action = serializers.JSONField(required=False, default={})
    denied_items = serializers.JSONField(required=False, default={})
    company_id = serializers.CharField(required=True)


class CompanyWithGroupsAndDeptsSerializer(serializers.Serializer):
    company = CompanySerializer()
    departments = FakeDepartmentSerializer(many=True, default=[])
