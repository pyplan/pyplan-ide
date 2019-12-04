from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from pyplan.pyplan.preference.serializers import PreferenceSerializer
from pyplan.pyplan.user_company_preference.service import \
    UserCompanyPreferenceService


from .models import UserCompany
from .permissions import UserCompanyPermissions
from .serializers import UserCompanySerializer, UserCompanyCreateUpdateSerializer, UserCompanyPartialUpdateSerializer, ListByCompanyIdSerializer
from .service import UserCompanyService
from .pagination import UserCompaniesPagination


class UserCompanyViewSet(viewsets.ModelViewSet):
    """
    Updates and retrieves user companies relations
    """
    queryset = UserCompany.objects.all()
    serializer_class = UserCompanySerializer
    permission_classes = (UserCompanyPermissions,)
    pagination_class = UserCompaniesPagination

    def list(self, request, *args, **kwargs):

        try:
            service = UserCompanyService(request)
            response = service.list()
            if len(response) > 0:
                return Response(UserCompanySerializer(response, many=True).data, status=status.HTTP_200_OK)
            return Response("There was an error in the list", status=status.HTTP_406_NOT_ACCEPTABLE)
        except Exception as ex:
            return Response(str({ex}), status=status.HTTP_406_NOT_ACCEPTABLE)

    def create(self, request, *args, **kwargs):

        try:
            serializer = UserCompanyCreateUpdateSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            service = UserCompanyService(request)
            response = service.create(serializer.validated_data)
            if len(response) > 0:
                return Response(UserCompanySerializer(response, many=True).data, status=status.HTTP_201_CREATED)
            return Response("There was an error in the creation", status=status.HTTP_406_NOT_ACCEPTABLE)
        except Exception as ex:
            return Response(str({ex}), status=status.HTTP_406_NOT_ACCEPTABLE)

    def update(self, request, *args, **kwargs):
        try:
            user_id = kwargs.get("pk")
            serializer = UserCompanyPartialUpdateSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            service = UserCompanyService(request)
            response = service.partial_update(user_id, serializer.validated_data)
            if response:
                return Response(UserCompanySerializer(response, many=True).data, status=status.HTTP_200_OK)
            return Response("There was an error in the update", status=status.HTTP_406_NOT_ACCEPTABLE)
        except Exception as ex:
            return Response(str({ex}), status=status.HTTP_406_NOT_ACCEPTABLE)

    def partial_update(self, request, *args, **kwargs):
        try:
            user_id = kwargs.get("pk")
            serializer = UserCompanyPartialUpdateSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            service = UserCompanyService(request)
            response = service.partial_update(user_id, serializer.validated_data)
            if response:
                return Response(UserCompanySerializer(response, many=True).data, status=status.HTTP_200_OK)
            return Response("There was an error in the update", status=status.HTTP_406_NOT_ACCEPTABLE)
        except Exception as ex:
            return Response(str({ex}), status=status.HTTP_406_NOT_ACCEPTABLE)

    @action(detail=False, methods=['get'])
    def preferences(self, request):
        preferences = UserCompanyPreferenceService(request).getUserCompanyPreferences()
        if preferences:
            return Response(PreferenceSerializer(preferences, many=True).data)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=['get'])
    def preference_by_code(self, request):
        code = str(request.query_params.get("code", None))
        if code:
            preference = UserCompanyPreferenceService(request).getUserCompanyPreference(code)
            if preference:
                return Response(PreferenceSerializer(preference).data)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=['get'])
    def list_by_company_id(self, request):
        try:
            service = UserCompanyService(request)
            users = service.listByCompanyId()
            if len(users) > 0:
                return Response(ListByCompanyIdSerializer(users, many=True).data)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as ex:
            return Response(str(ex), status=status.HTTP_406_NOT_ACCEPTABLE)
