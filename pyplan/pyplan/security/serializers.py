from pyplan.pyplan.modelmanager.classes.modelInfo import ModelInfo
from pyplan.pyplan.security.classes.clientSession import ClientSession
from pyplan.pyplan.modelmanager.serializers.ModelInfoSerializer import ModelInfoSerializer
from rest_framework import serializers


class ClientSessionSerializer(serializers.Serializer):
    session_key = serializers.CharField()
    userId = serializers.CharField()
    userFullName = serializers.CharField()
    userCompanyId = serializers.IntegerField()
    userIsSuperUser = serializers.BooleanField()
    companyId = serializers.IntegerField()
    company_code = serializers.CharField()
    companyName = serializers.CharField()
    process = serializers.ListField()
    modelInfo = ModelInfoSerializer()
    imageUrl = serializers.CharField(allow_blank=True)
    loginModule = serializers.CharField(allow_blank=True)
    autoopenUri = serializers.CharField(allow_blank=True)
    decimalSep = serializers.CharField(allow_blank=True)
    thousandSep = serializers.CharField(allow_blank=True)
    copyDecimalSep = serializers.CharField(allow_blank=True)
    companySettingFile = serializers.CharField(allow_blank=True)
    loginAction = serializers.JSONField(required=False, allow_null=True)
    created_at = serializers.DateTimeField(required=True, allow_null=False)
    departments = serializers.ListField(required=False, allow_null=True)
    my_uuid = serializers.UUIDField(allow_null=True, default=None)

    def create(self, validated_data):
        instance = ClientSession()
        instance.session_key = validated_data.get(
            'session_key', instance.session_key)
        instance.userId = validated_data.get('userId', instance.userId)
        instance.userFullName = validated_data.get(
            'userFullName', instance.userFullName)
        instance.userCompanyId = validated_data.get(
            'userCompanyId', instance.userCompanyId)
        instance.userIsSuperUser = validated_data.get(
            'userIsSuperUser', instance.userIsSuperUser)
        instance.companyId = validated_data.get(
            'companyId', instance.companyId)
        instance.company_code = validated_data.get(
            'company_code', instance.company_code)
        instance.companyName = validated_data.get(
            'companyName', instance.companyName)
        instance.process = validated_data.get('process', instance.process)
        instance.autoopenUri = validated_data.get(
            'autoopenUri', instance.autoopenUri)
        instance.decimalSep = validated_data.get(
            'decimalSep', instance.decimalSep)
        instance.thousandSep = validated_data.get(
            'thousandSep', instance.thousandSep)
        instance.copyDecimalSep = validated_data.get(
            'copyDecimalSep', instance.copyDecimalSep)
        instance.companySettingFile = validated_data.get(
            'companySettingFile', instance.companySettingFile)
        instance.loginAction = validated_data.get(
            'loginAction', instance.loginAction)
        instance.created_at = validated_data.get(
            'created_at', instance.created_at)
        instance.departments = validated_data.get(
            'departments', instance.departments)

        # fill modelInfo related object
        instance.modelInfo = ModelInfo()
        modelInfoSerializer = ModelInfoSerializer(
            data=validated_data.get('modelInfo', instance.modelInfo))
        modelInfoSerializer.is_valid(raise_exception=True)
        instance.modelInfo = modelInfoSerializer.save()

        return instance
