from rest_framework import serializers

from pyplan.pyplan.companies.serializers import CompanySerializer
from pyplan.pyplan.users.models import User
from pyplan.pyplan.users.serializers import (CreateUserFromUISerializer,
                                             UpdateUserFromUISerializer)

from .models import UserCompany


class UserCompanyCreateUpdateSerializer(serializers.Serializer):
    companies = serializers.ListField(child=serializers.JSONField(), required=True)
    user = CreateUserFromUISerializer(required=True)
    permissions = serializers.ListField(child=serializers.CharField(), default=[])

class UserCompanyPartialUpdateSerializer(serializers.Serializer):
    companies = serializers.ListField(child=serializers.JSONField(), default=[])
    user = UpdateUserFromUISerializer(required=False, allow_null=True)
    permissions = serializers.ListField(child=serializers.CharField(), default=[])

class UserCompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = UserCompany
        fields = '__all__'

class ListByCompanyIdSerializer(serializers.ModelSerializer):
    user_company_id = serializers.CharField()
    active = serializers.BooleanField()
    langCode = serializers.CharField()
    imageURL = serializers.CharField()
    companies = CompanySerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email',
                  'langCode', 'active', 'imageURL', 'companies', 'user_company_id')
        read_only_fields = ('username', )

class UsersCompaniesSerializer(serializers.ModelSerializer):
    user_company = UserCompanySerializer(many=True, default=[])
