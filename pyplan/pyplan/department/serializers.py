from rest_framework import serializers

from pyplan.pyplan.companies.serializers import CompanySerializer, LightCompanySerializer

from .models import Department


class DepartmentSerializer(serializers.ModelSerializer):
    company = CompanySerializer()
    engine_definitions = serializers.JSONField(required=False, default=None)
    login_action = serializers.JSONField(required=False, default=None)

    class Meta:
        model = Department
        fields = '__all__'

class LightDepartmentSerializer(serializers.ModelSerializer):
    company = LightCompanySerializer(default=None)

    class Meta:
        model = Department
        fields = ('id', 'code', 'name', 'company',)
        depth = 1

class DepartmentCreateUpdateSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=50, required=True)
    name = serializers.CharField(max_length=255, required=True)
    engine_definitions = serializers.JSONField(required=False, default={})
    login_action = serializers.JSONField(required=False, default={})
    denied_items = serializers.JSONField(required=False, default={})
    company_id = serializers.CharField(required=False)


class DepartmentPartialUpdateSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=50, required=True)
    name = serializers.CharField(max_length=255, required=False, default=None)
    engine_definitions = serializers.JSONField(required=False, default=None)
    login_action = serializers.JSONField(required=False, default=None)
    denied_items = serializers.JSONField(required=False, default=None)
    company_id = serializers.CharField(required=False)


class FolderOrModuleSerializer(serializers.Serializer):
    folder = serializers.CharField(required=False)
    module = serializers.CharField(required=False)


class DepartmentDenyItemsSerializer(FolderOrModuleSerializer):
    departments = serializers.ListField(child=serializers.IntegerField())
