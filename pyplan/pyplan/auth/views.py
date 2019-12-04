import base64
from datetime import timedelta

from django.conf import settings
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from django.utils import timezone
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from pyplan.pyplan.auth.serializers.passwordResetSerializer import \
    PasswordResetSerializer
from pyplan.pyplan.auth.serializers.sendPasswordResetEmailSerializer import \
    SendPasswordResetEmailSerializer
# enums
from pyplan.pyplan.common.email.classes.eEmailType import eEmailType
# services
from pyplan.pyplan.common.email.service import EmailService
# serializers
from pyplan.pyplan.companies.serializers import CompanySerializer
# models
from pyplan.pyplan.users.models import User


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data,
            context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        # token_expire_handler will check, if the token is expired it will generate new one
        is_expired, token = _TokenHelpers.token_expire_handler(token)
        companies = CompanySerializer(user.companies.all(), many=True).data
        return Response({
            'id': user.pk,
            'token': token.key,
            'email': user.email,
            'companies': companies,
        })

class SendPasswordResetEmail(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        try:

            serializer = SendPasswordResetEmailSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            username = serializer.validated_data['username']
            user = User.objects.get(username=username)
            token, created = Token.objects.get_or_create(user=user)
            # token_expire_handler will check, if the token is expired it will generate new one
            is_expired, token = _TokenHelpers.token_expire_handler(token)

            # A new token has been created, send a new email
            key = f"id={username}&static={token.key}"
            encriptedKey = str(base64.b64encode(key.encode()), "utf-8")
            link = f"{serializer.validated_data['publicUrl']}#resetpassword/query={encriptedKey}"
            email = {
                'email_to': user.email,
                'name_to': username,
                'email_type': eEmailType.RESET_PASSWORD,
                'context': {
                    "username": username,
                    "link": link
                }
            }
            service = EmailService(request)
            if service.addToQueue(email):
                if service.sendQueue():
                    return Response(True)
            return Response(False)
        except Exception as ex:
            return Response(True)

class PasswordReset(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        try:
            serializer = PasswordResetSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            query = serializer.validated_data['query'][6:].encode()
            decriptedQuery = base64.decodestring(query).decode()
            username = decriptedQuery[3:decriptedQuery.find('&')]
            static = decriptedQuery[decriptedQuery.find('&')+8:]

            user = User.objects.get(username=username)
            token = Token.objects.get(key=static)
            if not _TokenHelpers.is_token_expired(token):
                newPassword = BaseUserManager().make_random_password(8)
                hasshedPassword = make_password(newPassword)
                user.password = hasshedPassword
                user.save()
                email = {
                    'email_to': user.email,
                    'name_to': username,
                    'email_type': eEmailType.CHANGED_PASSWORD,
                    'context': {
                        "username": username,
                        "password": newPassword
                    }
                }
                service = EmailService(request)
                if service.addToQueue(email):
                    if service.sendQueue():
                        return Response(True)
                return Response(False)
            return Response(False)
        except Exception as ex:
            return Response(False)


class _TokenHelpers():

    is_expired = False

    # this return left time
    @classmethod
    def expires_in(cls, token):
        time_elapsed = timezone.now() - token.created
        left_time = timedelta(seconds=settings.TOKEN_EXPIRED_AFTER_SECONDS) - time_elapsed
        return left_time

    # token checker if token expired or not
    @classmethod
    def is_token_expired(cls, token):
        return cls.expires_in(token) < timedelta(seconds=0)

    # if token is expired new token will be established
    # If token is expired then it will be removed
    # and new one with different key will be created
    @classmethod
    def token_expire_handler(cls, token):
        cls.is_expired = cls.is_token_expired(token)
        if cls.is_expired:
            token.delete()
            token = Token.objects.create(user=token.user)
        return cls.is_expired, token
