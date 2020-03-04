from rest_framework import serializers

from pyplan.pyplan.companies.models import Company
from pyplan.pyplan.companies.serializers import (CompanySerializer,
                                                 LightCompanySerializer)
from pyplan.pyplan.department.models import Department
from pyplan.pyplan.department.serializers import LightDepartmentSerializer

from .models import User


class UserSerializer(serializers.ModelSerializer):
    active = serializers.BooleanField()
    langCode = serializers.CharField()
    imageURL = serializers.CharField()
    companies = serializers.SerializerMethodField(read_only=True, default=[])
    departments = serializers.SerializerMethodField(required=False, default=[])

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email',
                  'langCode', 'active', 'last_login', 'imageURL', 'companies', 'departments',)
        read_only_fields = ('username', )

    def get_companies(self, obj):
        request = self.context.get('request')
        queryset = Company.objects.filter(users__pk=obj.pk)
        if not (request.user.is_superuser or request.user.is_staff):
            queryset = queryset.filter(
                pk__in=request.user.companies.values_list('id', flat=True))
        return LightCompanySerializer(queryset, many=True).data

    def get_departments(self, obj):
        request = self.context.get('request')
        queryset = Department.objects.filter(usercompanies__user__pk=obj.pk)
        if not (request.user.is_superuser or request.user.is_staff):
            queryset = queryset.filter(
                company__pk__in=request.user.companies.values_list('id', flat=True))
        return LightDepartmentSerializer(queryset, many=True).data


class LightUserSerializer(serializers.ModelSerializer):
    active = serializers.BooleanField()
    langCode = serializers.CharField()
    imageURL = serializers.CharField()

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email',
                  'langCode', 'active', 'last_login', 'imageURL', 'companies', 'my_uuid', 'my_username')
        read_only_fields = ('username', )


class UpdateUserFromUISerializer(serializers.Serializer):
    id = serializers.CharField(required=False, allow_null=True)
    username = serializers.CharField(required=False, allow_null=True)
    first_name = serializers.CharField(required=False, allow_null=True)
    last_name = serializers.CharField(required=False, allow_null=True)
    email = serializers.CharField(required=False, allow_null=True)
    password = serializers.CharField(required=False, allow_null=True)
    active = serializers.BooleanField(required=False, allow_null=True)
    last_login = serializers.DateTimeField(required=False, allow_null=True)
    langCode = serializers.CharField(required=False, allow_null=True)
    imageURL = serializers.CharField(required=False, allow_null=True)
    companies = CompanySerializer(many=True, required=False, default=[])


class CreateUserFromUISerializer(serializers.ModelSerializer):
    active = serializers.BooleanField()
    langCode = serializers.CharField(required=False)
    imageURL = serializers.CharField(required=False)
    companies = CompanySerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email',
                  'langCode', 'active', 'last_login', 'imageURL', 'companies', 'password')


class CreateUserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        # call create_user on user object. Without this
        # the password will be stored in plain text.
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name',
                  'last_name', 'email', 'auth_token',)
        read_only_fields = ('auth_token',)
        extra_kwargs = {'password': {'write_only': True}}


class UpdateUserSerializer(serializers.ModelSerializer):
    id = serializers.CharField(required=True)
    first_name = serializers.CharField(max_length=30, allow_null=True, required=False, allow_blank=True)
    last_name = serializers.CharField(max_length=30, allow_null=True, required=False, allow_blank=True)
    email = serializers.EmailField(required=False)
    langCode = serializers.CharField(max_length=10, allow_null=True, required=False)
    password = serializers.CharField(allow_null=True, required=False, allow_blank=True)

    def update(self, request, validated_data):
        user = User.objects.get(pk=validated_data['id'])
        if validated_data['first_name']:
            user.first_name = validated_data['first_name']
        if validated_data['last_name']:
            user.last_name = validated_data['last_name']
        if validated_data['email']:
            user.email = validated_data['email']
        if validated_data['langCode']:
            user.langCode = validated_data['langCode']
        if validated_data['password'] and validated_data['password'] != '':
            user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'langCode',
                  'first_name', 'last_name', 'email', 'auth_token',)
        read_only_fields = ('auth_token',)
        extra_kwargs = {'password': {'write_only': False}}
