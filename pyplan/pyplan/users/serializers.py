from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from .models import User
from pyplan.pyplan.companies.serializers import CompanySerializer


class UserSerializer(serializers.ModelSerializer):
    active = serializers.BooleanField()
    langCode = serializers.CharField()
    imageURL = serializers.CharField()
    companies = CompanySerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email',
                  'langCode', 'active', 'last_login', 'imageURL', 'companies',)
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

# cant import any serializers from department serializers due to circular references with the company serializer


class FakeDepartmentSerializer(serializers.Serializer):
    id = serializers.CharField(required=True)
    code = serializers.CharField(max_length=50, required=True)
    name = serializers.CharField(max_length=255, required=True)
    engine_definitions = serializers.JSONField(required=False, default={})
    login_action = serializers.JSONField(required=False, default={})
    denied_items = serializers.JSONField(required=False, default={})
    company_id = serializers.CharField(required=True)


class AssignedCompaniesSerializer(serializers.Serializer):
    id = serializers.CharField()
    code = serializers.CharField()
    name = serializers.CharField()
    system = serializers.CharField()
    active = serializers.BooleanField()
    licence = serializers.CharField()
    departments = FakeDepartmentSerializer(many=True, default=[])


class FullUserSerializer(serializers.Serializer):
    id = serializers.CharField()
    username = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.CharField()
    active = serializers.BooleanField()
    last_login = serializers.DateTimeField()
    langCode = serializers.CharField()
    imageURL = serializers.CharField()
    companies = CompanySerializer(many=True)
    assigned = AssignedCompaniesSerializer(many=True)


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
    first_name = serializers.CharField(
        max_length=30, allow_null=True, required=False, allow_blank=True)
    last_name = serializers.CharField(
        max_length=30, allow_null=True, required=False, allow_blank=True)
    email = serializers.EmailField(required=False)
    langCode = serializers.CharField(
        max_length=10, allow_null=True, required=False)
    password = serializers.CharField(
        allow_null=True, required=False, allow_blank=True)

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
