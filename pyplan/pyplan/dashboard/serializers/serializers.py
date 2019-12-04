from rest_framework import serializers

from pyplan.pyplan.common.classes.filterChoices import filterChoices
from pyplan.pyplan.dashboardstyle.serializers import DashboardStyleSerializer
from pyplan.pyplan.department.serializers import DepartmentSerializer
from pyplan.pyplan.usercompanies.serializers import UserCompanySerializer
from pyplan.pyplan.users.serializers import UserSerializer

from ..models import Dashboard


class DashboardCreateSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, max_length=255)
    reportId = serializers.IntegerField(allow_null=True)
    definition = serializers.JSONField(required=False)

class DashboardUpdateSerializer(serializers.Serializer):
    name = serializers.CharField(required=False, max_length=255)
    report_id = serializers.IntegerField(source="reportId", required=False)
    definition = serializers.JSONField(required=False)
    styles = serializers.ListField(child=serializers.IntegerField(), default=[])

class DashboardSerializer(serializers.Serializer):
    dashItemId = serializers.IntegerField(source="id")
    reportItemId = serializers.IntegerField(source="report.id", required=False)
    model = serializers.CharField()
    name = serializers.CharField()
    definition = serializers.JSONField(required=False, default={})
    order = serializers.IntegerField()

    isFav = serializers.BooleanField(source="is_fav", required=False, default=False)
    sharedToEveryone = serializers.BooleanField(source="is_public", required=False, default=False)
    node = serializers.CharField(required=False, allow_null=True)
    owner = serializers.IntegerField(source="owner.id", required=False)

    parentId = serializers.IntegerField(source="report.parent_id", required=False, default=None)
    isShared = serializers.SerializerMethodField(required=False, default=False)
    sharedBy = serializers.SerializerMethodField(required=False, default=None)
    ownerName = serializers.SerializerMethodField(required=False, default=None)

    dashVersion = serializers.SerializerMethodField(required=False, default=1)

    def get_isShared(self, obj):
        current_user_companies = self.context.get("request").user.usercompanies.values_list('pk', flat=True)
        is_owner = obj.owner_id in current_user_companies
        return not is_owner and (obj.usercompanies.count() > 0 or obj.departments.count() > 0 or obj.is_public)

    def get_sharedBy(self, obj):
        current_user_companies = self.context.get("request").user.usercompanies.values_list('pk', flat=True)
        is_owner = obj.owner_id in current_user_companies
        if not is_owner and (obj.usercompanies.count() > 0 or obj.departments.count() > 0 or obj.is_public):
            return obj.owner.user.first_name
        return None

    def get_ownerName(self, obj):
        if not obj.owner.user_id is None:
            return obj.owner.user.first_name
        return ""

    def get_dashVersion(self, obj):
        if obj.definition and str(obj.definition).startswith("{'type'"):
            return 0
        return 1

class DashboardExportSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    report_id = serializers.IntegerField(source="report.id", required=False)
    owner_id = serializers.IntegerField(required=False)

    model = serializers.CharField()
    node = serializers.CharField(required=False, allow_null=True)
    name = serializers.CharField()
    order = serializers.IntegerField()

    is_fav = serializers.BooleanField(required=False, default=False)
    is_public = serializers.BooleanField(required=False, default=False)
    definition = serializers.JSONField(required=False, default={})
    styles = serializers.SerializerMethodField(required=False, default=False)

    parent_id = serializers.IntegerField(source="report.parent_id", required=False, default=None)
    is_shared = serializers.SerializerMethodField(required=False, default=False)

    def get_is_shared(self, obj):
        return obj.usercompanies.count() > 0

    def get_styles(self, obj):
        return list(map(lambda item: item, obj.styles.values_list('id', flat=True))) if obj.styles else []

class DashboardImportSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    report_id = serializers.IntegerField(required=False, allow_null=True)
    owner_id = serializers.IntegerField(required=False)

    model = serializers.CharField(required=False)
    node = serializers.CharField(required=False, allow_null=True)
    name = serializers.CharField()
    order = serializers.IntegerField(required=False)

    is_fav = serializers.BooleanField(required=False, default=False)
    is_public = serializers.BooleanField(required=False, default=False)
    definition = serializers.JSONField(required=False, default={}, allow_null=True)
    styles = serializers.ListField(child=serializers.IntegerField(), default=[])

    parent_id = serializers.IntegerField(required=False, allow_null=True)
    is_shared = serializers.BooleanField(required=False, default=False)
    shared_by = serializers.ListSerializer(child=serializers.IntegerField(), required=False, default=[])

class DashboardModelSerializer(serializers.ModelSerializer):
    dashItemId = serializers.IntegerField(source="id")
    reportItemId = serializers.IntegerField(source="report.id", required=False)
    model = serializers.CharField()
    name = serializers.CharField()
    node = serializers.CharField()
    owner = serializers.IntegerField(source="owner.id", required=False)
    definition = serializers.JSONField(required=False, default={})

    parentId = serializers.CharField(source="report.parent_id", required=False)
    isFav = serializers.BooleanField(source="is_fav", required=False, default=False)
    sharedToEveryone = serializers.BooleanField(source="is_public", required=False, default=False)
    isShared = serializers.SerializerMethodField(required=False, default=False)
    sharedBy = serializers.SerializerMethodField(required=False, default=None)

    def get_isShared(self, obj):
        current_user_companies = self.context.get("request").user.usercompanies.values_list('pk', flat=True)
        is_owner = obj.owner_id in current_user_companies
        return not is_owner and (obj.usercompanies.count() > 0 or obj.departments.count() > 0 or obj.is_public)

    def get_sharedBy(self, obj):
        current_user_companies = self.context.get("request").user.usercompanies.values_list('pk', flat=True)
        is_owner = obj.owner_id in current_user_companies
        if not is_owner and (obj.usercompanies.count() > 0 or obj.departments.count() > 0 or obj.is_public):
            return obj.owner.user.first_name
        return None

    class Meta:
        model = Dashboard
        fields = '__all__'


class DashboardGetSerializer(serializers.Serializer):
    dashboardId = serializers.IntegerField(source="id")
    companyId = serializers.IntegerField(source="owner.company.id", required=False)
    name = serializers.CharField()
    node = serializers.CharField()
    ownerId = serializers.IntegerField(source="owner.id", required=False)

    definition = serializers.JSONField(required=False, default={})

    parentId = serializers.CharField(source="report.parent_id", required=False)
    isFav = serializers.BooleanField(source="is_fav", required=False, default=False)

    sharedToEveryone = serializers.BooleanField(source="is_public", required=False, default=False)
    isShared = serializers.SerializerMethodField(required=False, default=False)
    sharedBy = serializers.SerializerMethodField(required=False, default=None)

    styleLibraries = DashboardStyleSerializer(source='styles', many=True)

    def get_isShared(self, obj):
        current_user_companies = self.context.get("request").user.usercompanies.values_list('pk', flat=True)
        is_owner = obj.owner_id in current_user_companies
        return not is_owner and (obj.usercompanies.count() > 0 or obj.departments.count() > 0 or obj.is_public)

    def get_sharedBy(self, obj):
        current_user_companies = self.context.get("request").user.usercompanies.values_list('pk', flat=True)
        is_owner = obj.owner_id in current_user_companies
        if not is_owner and (obj.usercompanies.count() > 0 or obj.departments.count() > 0 or obj.is_public):
            return obj.owner.user.first_name
        return None

class DashboardGetIndexValuesSerializer(serializers.Serializer):
    id = serializers.CharField()
    filter = serializers.ChoiceField(required=False, choices=[(e.value, e.name) for e in filterChoices])
    text1 = serializers.CharField(required=False)
    text2 = serializers.CharField(required=False)
    page = serializers.IntegerField(required=False)

class UserCompanyGetSharesSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    user = UserSerializer()

class DepartmentGetSharesSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    code = serializers.CharField()
    name = serializers.CharField()
    usercompanies = UserCompanyGetSharesSerializer(many=True)

class DashboardGetSharesSerializer(serializers.Serializer):
    departments_shares = DepartmentSerializer(many=True)
    usercompanies_shares = UserCompanySerializer(many=True)
    departments = DepartmentGetSharesSerializer(many=True)
    sharedToEveryone = serializers.BooleanField(default=False)
    sharedTo = serializers.BooleanField(default=False)
    noShared = serializers.BooleanField(default=False)

class DashboarSetSharesSerializer(serializers.Serializer):
    usercompanies_ids = serializers.ListField(required=False, child=serializers.IntegerField())
    departments_ids = serializers.ListField(required=False, child=serializers.IntegerField())
    noShared = serializers.BooleanField(default=False)
    sharedToEveryone = serializers.BooleanField(default=False)
    sharedTo = serializers.BooleanField(default=False)
