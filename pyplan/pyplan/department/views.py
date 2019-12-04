from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Department
from .permissions import DepartmentPermissions
from .serializers import (DepartmentDenyItemsSerializer, DepartmentSerializer,
                          FolderOrModuleSerializer, DepartmentCreateUpdateSerializer, DepartmentPartialUpdateSerializer)
from .service import DepartmentService


class DepartmentViewSet(viewsets.ModelViewSet):
    """
    Updates and retrieves Department relations
    """
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = (DepartmentPermissions,)
    pagination_class = None

    def list(self, request, *args, **kwargs):
        try:
            service = DepartmentService(request)
            response = service.list()
            if len(response) > 0:
                return Response(DepartmentSerializer(response, many=True).data)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as ex:
            return Response(str({ex}), status=status.HTTP_406_NOT_ACCEPTABLE)

    def create(self, request, *args, **kwargs):
        try:
            serializer = DepartmentCreateUpdateSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            service = DepartmentService(request)
            response = service.create(serializer.validated_data)
            if response:
                return Response(DepartmentSerializer(response).data)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as ex:
            return Response(str({ex}), status=status.HTTP_406_NOT_ACCEPTABLE)

    def partial_update(self, request, *args, **kwargs):
        try:
            department_id = kwargs.get("pk")
            serializer = DepartmentPartialUpdateSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            service = DepartmentService(request)
            response = service.partial_update(department_id, serializer.validated_data)
            if response:
                return Response(DepartmentSerializer(response).data)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as ex:
            return Response(str({ex}), status=status.HTTP_406_NOT_ACCEPTABLE)

    @action(methods=['get'], detail=False)
    def by_current_company(self, request):
        service = DepartmentService(self.request)
        departments = service.byCurrentCompany()
        if departments:
            return Response(DepartmentSerializer(departments, many=True).data)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(methods=['get'], detail=False)
    def denied(self, request):
        """
        Denied departments of given folder name
        """
        serialized_rq = FolderOrModuleSerializer(data=request.query_params)
        serialized_rq.is_valid(raise_exception=True)

        service = DepartmentService(self.request)
        departments = service.deniedByItem(serialized_rq.validated_data)
        if departments:
            return Response(DepartmentSerializer(departments, many=True).data)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(methods=['post'], detail=False)
    def deny_items(self, request):
        """
        Set denied folder or module for departments
        """
        serialized_rq = DepartmentDenyItemsSerializer(data=request.data)
        serialized_rq.is_valid(raise_exception=True)
        service = DepartmentService(self.request)
        departments = service.denyItems(serialized_rq.validated_data)
        return Response(DepartmentSerializer(departments, many=True).data)
