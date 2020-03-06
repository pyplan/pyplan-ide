from rest_framework import status, viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from .models import User
from .pagination import UserPagination
from .permissions import UserPermissions
from .serializers import (CreateUserSerializer, UpdateUserSerializer,
                          UserSerializer)
from .service import UserService


class UserViewSet(viewsets.ModelViewSet):
    """
    Users CRUD
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = UserPagination

    def list(self, request, *args, **kwargs):
        try:
            service = UserService(request)
            response = service.list()
            if len(response) > 0:
                return Response(UserSerializer(response, many=True, context={'request': request}).data, status=status.HTTP_200_OK)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as ex:
            return Response(str({ex}), status=status.HTTP_406_NOT_ACCEPTABLE)

    def retrieve(self, request, *args, **kwargs):
        try:
            user_id = kwargs.get("pk")
            if user_id:
                service = UserService(request)
                response = service.retrieve(user_id)
                return Response(UserSerializer(response, context={'request': request}).data, status=status.HTTP_200_OK)
            return Response("Could not find user id ", status=status.HTTP_406_NOT_ACCEPTABLE)
        except Exception as ex:
            return Response(str({ex}), status=status.HTTP_406_NOT_ACCEPTABLE)

    def partial_update(self, request, *args, **kwargs):
        try:
            user_id = kwargs.get("pk")
            if user_id:
                service = UserService(request)
                response = service.partial_update(user_id, request.data)
                return Response(UserSerializer(response, context={'request': request}).data, status=status.HTTP_200_OK)
            return Response("Could not find user id ", status=status.HTTP_406_NOT_ACCEPTABLE)
        except Exception as ex:
            return Response(str({ex}), status=status.HTTP_406_NOT_ACCEPTABLE)

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [IsAdminUser, ]
        else:
            self.permission_classes = [UserPermissions, ]
        return super(UserViewSet, self).get_permissions()
