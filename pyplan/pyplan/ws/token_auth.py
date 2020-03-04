from importlib import import_module

from channels.auth import AuthMiddlewareStack
from django.conf import settings
from django.contrib.auth.models import AnonymousUser
from django.db import close_old_connections
from rest_framework.authtoken.models import Token

from pyplan.pyplan.users.models import User


class TokenAuthMiddleware:
    """
    Token authorization middleware for Django Channels 2
    """

    def __init__(self, inner):
        self.inner = inner

    def __call__(self, scope):
        # headers = dict(scope['headers'])
        if scope['query_string']:
            qs_name, qs_value = scope['query_string'].decode().split('=')
            if qs_name == 'apiKey':
                try:
                    if qs_value:
                        token = Token.objects.get(key=qs_value)
                        scope['user'] = token.user
                        close_old_connections()
                except Token.DoesNotExist:
                    scope['user'] = AnonymousUser()
            elif qs_name == 'sessionKey':
                try:
                    if qs_value:
                        scope['user'] = self.userFromSession(qs_value)
                        close_old_connections()
                except Exception:
                    scope['user'] = AnonymousUser()
        return self.inner(scope)

    def userFromSession(self, session_key):
        session_engine = import_module(settings.SESSION_ENGINE)
        session_wrapper = session_engine.SessionStore(session_key)
        session = session_wrapper.load()
        user_id = session.get('data').get('userId')

        if user_id:
            user = User.objects.get(pk=session.get('data').get('userId'))
            if user:
                return user
        return AnonymousUser()


def TokenAuthMiddlewareStack(inner): return TokenAuthMiddleware(
    AuthMiddlewareStack(inner))
