from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from pyplan.pyplan.company_preference.service import CompanyPreferenceService
from pyplan.pyplan.preference.serializers import PreferenceSerializer

from .models import Company
from .pagination import CompanyPagination
from .permissions import CompanyPermissions
from .serializers import (CompanySerializer, CreateCompanySerializer,
                          FullCompanySerializer, UpdateCompanySerializer)
from .service import CompaniesService


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

    def list(self, request, *args, **kwargs):
        try:
            service = CompaniesService(request)
            queryset = service.list()
            if queryset:
                page = self.paginate_queryset(queryset)
                if page is not None:
                    serializer = FullCompanySerializer(page, many=True)
                    return self.get_paginated_response(serializer.data)
                return Response(FullCompanySerializer(queryset, many=True).data)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as ex:
            return Response(str(ex), status=status.HTTP_406_NOT_ACCEPTABLE)

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
