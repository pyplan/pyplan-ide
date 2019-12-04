from rest_framework.authentication import TokenAuthentication


class QueryStringTokenAuthentication(TokenAuthentication):
    """
    Extend the TokenAuthentication class to support querystring authentication
    in the form of "http://api.pyplan.com/?auth_token=<token_key>"
    """

    def authenticate(self, request):
        # Check if 'token_auth' is in the request query params.
        # Give precedence to 'Authorization' header.
        if 'auth_token' in request.query_params and \
            'session_key' in request.query_params and \
            'HTTP_AUTHORIZATION' not in request.META and \
                'HTTP_SESSION_KEY' not in request.META:
            request.META['HTTP_AUTHORIZATION'] = request.query_params.get('auth_token')
            request.META['HTTP_SESSION_KEY'] = request.query_params.get('session_key')
            return self.authenticate_credentials(request.query_params.get('auth_token'))
        else:
            return super(QueryStringTokenAuthentication, self).authenticate(request)
