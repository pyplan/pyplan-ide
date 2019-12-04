from rest_framework import serializers

from pyplan.pyplan.common.serializers.RecursiveField import RecursiveField
from pyplan.pyplan.dashboard.serializers.serializers import (
    DashboardExportSerializer, DashboardImportSerializer, DashboardSerializer)
from pyplan.pyplan.dashboardstyle.serializers import (
    DashboardStyleImportSerializer, DashboardStyleSerializer)
from pyplan.pyplan.department.serializers import DepartmentSerializer
from pyplan.pyplan.usercompanies.serializers import UserCompanySerializer
from pyplan.pyplan.users.serializers import UserSerializer

from .models import Report


class ReportCreateUpdateSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, max_length=255)
    parentId = serializers.IntegerField(required=False, default=None, allow_null=True)

    is_fav = serializers.BooleanField(source="isFav", required=False, default=False)
    is_public = serializers.BooleanField(source="isPublic", required=False, default=False)

class ReportSerializer(serializers.Serializer):
    reportItemId = serializers.IntegerField(source="id")
    model = serializers.CharField()
    name = serializers.CharField()
    order = serializers.IntegerField()

    sharedToEveryone = serializers.BooleanField(source="is_public", required=False, default=False)
    isFav = serializers.BooleanField(source="is_fav", required=False, default=False)
    owner = serializers.IntegerField(source="owner.id", required=False)

    parentId = serializers.IntegerField(source="parent_id", required=False, allow_null=True)
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

class ReportNavigatorItemSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()

class ReportGetNavigatorSerializer(serializers.Serializer):
    priorId = serializers.IntegerField()
    nextId = serializers.IntegerField()
    priorName = serializers.CharField()
    nextName = serializers.CharField()
    list = ReportNavigatorItemSerializer(many=True, default=[])

class ReportExportSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    model = serializers.CharField()
    name = serializers.CharField()
    order = serializers.IntegerField()
    is_public = serializers.BooleanField(required=False, default=False)
    is_fav = serializers.BooleanField(required=False, default=False)
    parent_id = serializers.IntegerField(required=False, allow_null=True)
    owner_id = serializers.IntegerField(required=False)
    is_shared = serializers.SerializerMethodField(required=False, default=False)
    dashboards = DashboardExportSerializer(many=True, default=[])
    reports = RecursiveField(many=True, default=[])

    def get_is_shared(self, obj):
        return obj.usercompanies.count() > 0

class ReportImportSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    model = serializers.CharField(required=False)
    name = serializers.CharField()
    order = serializers.IntegerField(required=False)
    is_public = serializers.BooleanField(required=False, default=False)
    is_fav = serializers.BooleanField(required=False, default=False)
    parent_id = serializers.IntegerField(required=False, allow_null=True)
    owner_id = serializers.IntegerField(required=False)
    is_shared = serializers.BooleanField(required=False, default=False)
    shared_by = serializers.ListSerializer(child=serializers.IntegerField(), required=False, default=[])
    dashboards = DashboardImportSerializer(many=True, default=[])
    reports = RecursiveField(many=True, default=[])

class SearchResultSerializer(serializers.Serializer):
    reports = ReportSerializer(many=True)
    dashboards = DashboardSerializer(many=True)

class DuplicateItemsSerializer(serializers.Serializer):
    report_ids = serializers.ListSerializer(child=serializers.IntegerField(), default=[])
    dashboard_ids = serializers.ListSerializer(child=serializers.IntegerField(), default=[])

class SetAsFavSerializer(DuplicateItemsSerializer):
    is_fav = serializers.BooleanField()

class ExportItemsSerializer(serializers.Serializer):
    reports = ReportExportSerializer(many=True)
    dashboards = DashboardExportSerializer(many=True, default=[])
    styles = DashboardStyleSerializer(many=True)

class ImportItemsSerializer(serializers.Serializer):
    reports = ReportImportSerializer(many=True)
    dashboards = DashboardImportSerializer(many=True)
    styles = DashboardStyleImportSerializer(many=True)

class UserCompanyGetSharesSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    user = UserSerializer()

class DepartmentGetSharesSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    code = serializers.CharField()
    name = serializers.CharField()
    usercompanies = UserCompanyGetSharesSerializer(many=True)

class ReportGetSharesSerializer(serializers.Serializer):
    departments_shares = DepartmentSerializer(many=True)
    usercompanies_shares = UserCompanySerializer(many=True)
    departments = DepartmentGetSharesSerializer(many=True)
    sharedToEveryone = serializers.BooleanField(default=False)
    sharedTo = serializers.BooleanField(default=False)
    noShared = serializers.BooleanField(default=False)

class ReportSetSharesSerializer(serializers.Serializer):
    usercompanies_ids = serializers.ListField(required=False, child=serializers.IntegerField())
    departments_ids = serializers.ListField(required=False, child=serializers.IntegerField())
    noShared = serializers.BooleanField(default=False)
    sharedToEveryone = serializers.BooleanField(default=False)
    sharedTo = serializers.BooleanField(default=False)
