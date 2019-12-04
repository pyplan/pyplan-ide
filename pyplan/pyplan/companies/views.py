from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from pyplan.pyplan.company_preference.service import CompanyPreferenceService
from pyplan.pyplan.preference.serializers import PreferenceSerializer

from .models import Company
from .permissions import CompanyPermissions
from .serializers import CompanySerializer, CreateCompanySerializer, CompanyWithGroupsAndDeptsSerializer, UpdateCompanySerializer
from .service import CompaniesService
from .pagination import CompanyPagination


class CompanyViewSet(viewsets.ModelViewSet):
    """
    Updates and retrieves companies
    """
    queryset = Company.objects.all()
    permission_classes = (CompanyPermissions,)
    pagination_class = CompanyPagination

    def get_serializer_class(self):
        if self.action in ['create']:
            return CreateCompanySerializer
        elif self.action in ['update', 'partial_update']:
            return UpdateCompanySerializer
        return CompanySerializer

    @action(methods=['get'], detail=False)
    def list_with_groups_and_depts(self, request):
        try:
            service = CompaniesService(request)
            response = service.list_with_groups_and_depts()
            if len(response) > 0:
                return Response(CompanyWithGroupsAndDeptsSerializer(response, many=True).data)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as ex:
            return Response(str(ex), status.HTTP_406_NOT_ACCEPTABLE)

    @action(methods=['get'], detail=False)
    def preferences(self, request):
        preferences = CompanyPreferenceService(request).getCompanyPreferences()
        if preferences:
            return Response(PreferenceSerializer(preferences, many=True).data)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(methods=['get'], detail=False)
    def preference_by_code(self, request):
        code = str(request.query_params.get("code", None))
        if code:
            preference = CompanyPreferenceService(request).getCompanyPreference(code)
            if preference:
                return Response(PreferenceSerializer(preference).data)
        return Response(status=status.HTTP_204_NO_CONTENT)
