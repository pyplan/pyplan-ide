import coreapi
from django.contrib.auth import logout
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
from django.urls import path
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, schema
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.schemas import AutoSchema

from pyplan.pyplan.common.logger import PyplanLogger
from pyplan.pyplan.filemanager.service import FileManagerService
from pyplan.pyplan.security.classes.activeSession import \
    ActiveSessionSerializer
from pyplan.pyplan.security.serializers import ClientSessionSerializer
from pyplan.pyplan.security.service import SecurityService


class SecurityView(object):
    """
    Perform security actions
    """

    @staticmethod
    def register():
        return [
            path('security/createSession', SecurityView.createSession),
            path('security/getSession', SecurityView.getSession),
            path('security/logout/', SecurityView.logout),
            path('security/getAllSessions/', SecurityView.getAllSessions),
            path('security/getMySessions/', SecurityView.getMySessions),
            path('security/killSessionByKey/', SecurityView.killSessionByKey),
            path('security/createNewSession/', SecurityView.createNewSession),
            path('security/useExternalLink/', SecurityView.useExternalLink),
            path('security/getSystemResources/',
                 SecurityView.getSystemResources)

        ]

    @staticmethod
    @api_view(['POST'])
    @schema(AutoSchema(manual_fields=[
        coreapi.Field("companyId", required=True,
                      description="Company to login")
    ]))
    def createSession(request, *args, **kargs):
        companyId = int(request.data.get("companyId", -1))
        security_service = SecurityService(request)
        clientSession = security_service.createSession(companyId)
        # Ensure User Workspace
        FileManagerService(request, clientSession).ensureUserWorkspace()

        serializer = ClientSessionSerializer(clientSession)

        PyplanLogger().logInfo(request, clientSession,
                               {'session_created': True})

        security_service.setStatistics()

        return Response(serializer.data)

    @staticmethod
    @api_view(['POST'])
    @permission_classes((IsAuthenticated,))
    @schema(AutoSchema(manual_fields=[]))
    def getSession(request, *args, **kargs):
        clientSession = SecurityService(request).getSession()

        serializer = ClientSessionSerializer(clientSession)
        return Response(serializer.data)

    @staticmethod
    @api_view(['GET'])
    @permission_classes((IsAuthenticated,))
    @schema(AutoSchema(manual_fields=[]))
    def getAllSessions(request, *args, **kargs):
        result = SecurityService(request).getAllSessions()
        return Response(ActiveSessionSerializer(result, many=True).data)

    @staticmethod
    @api_view(['GET'])
    @permission_classes((IsAuthenticated,))
    @schema(AutoSchema(manual_fields=[]))
    def getMySessions(request, *args, **kargs):
        result = SecurityService(request).getAllSessions(onlyMySessions=True)
        return Response(ActiveSessionSerializer(result, many=True).data)

    @staticmethod
    @api_view(['GET'])
    @permission_classes((IsAuthenticated,))
    @schema(AutoSchema(manual_fields=[
        coreapi.Field("session_key", required=True,
                      description="Session key to kill session")
    ]))
    def killSessionByKey(request, *args, **kargs):
        key = request.query_params.get("session_key")
        result = SecurityService(request).killSessionByKey(key)
        return Response(status=status.HTTP_200_OK)

    @staticmethod
    @api_view(['GET'])
    @permission_classes((IsAuthenticated,))
    @schema(AutoSchema())
    def logout(request, *args, **kargs):
        service = SecurityService(request)
        if service.client_session:
            service.logout()
        request.user.auth_token.delete()
        response = logout(request)
        PyplanLogger().logEndSession(request, service.client_session)

        return Response(status=status.HTTP_200_OK)

    @staticmethod
    @api_view(['GET'])
    @permission_classes((IsAuthenticated,))
    def createNewSession(request, *args, **kargs):
        result = SecurityService(request).createNewSession()
        serializer = ClientSessionSerializer(result)
        return Response(serializer.data)

    @staticmethod
    @api_view(['GET'])
    @permission_classes((AllowAny,))
    def useExternalLink(request, *args, **kargs):
        """
        Allows to login as guest and returns the entity_id,
        which could be a dashboard_id, report_id or node_id
        """
        guid = request.query_params.get("guid", None)
        if guid:
            service = SecurityService(request)
            try:
                session, token, entity_id, entity_type, extra_data = service.useExternalLink(
                    guid)
                # extra_data returns an array of dashboard_id's in case of a report external link
                return Response({
                    "entity_id": entity_id,
                    "entity_type": entity_type,
                    "session": ClientSessionSerializer(session).data,
                    "token": token.key,
                    "extra_data": extra_data,
                })
            except ObjectDoesNotExist as ex:
                return Response(
                    data={"error": "ExternalLink does not exist.",
                          "message": str(ex)},
                    status=status.HTTP_400_BAD_REQUEST
                )
            except MultipleObjectsReturned as ex:
                return Response(
                    data={"error": "Multiple results obtained.",
                          "message": str(ex)},
                    status=status.HTTP_400_BAD_REQUEST
                )
            except Exception as ex:
                return Response(
                    data={"message": str(ex)},
                    status=status.HTTP_400_BAD_REQUEST
                )
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    @api_view(['GET'])
    @permission_classes((IsAuthenticated,))
    @schema(AutoSchema(manual_fields=[
        coreapi.Field("session_key", required=False,
                      description="Session key to get resources")
    ]))
    def getSystemResources(request, *args, **kargs):
        key = request.query_params.get("session_key", None)
        return Response(SecurityService(request).getSystemResources(key))
