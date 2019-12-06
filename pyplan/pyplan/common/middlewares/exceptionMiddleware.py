from django.contrib import messages

from django.http import HttpResponse

from rest_framework import status


class ExceptionMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        response = self.get_response(request)

        return response

    def process_exception(self, request, exception):
        if isinstance(exception, ValueError):
            message = str(exception)
            if 'no module named' in message.lower():
                library = message[message.rfind(
                    "'", 0, message.rfind("'"))+1:message.rfind("'")]
                return HttpResponse(f'{message}. Please install "{library}" library using the Install Library utility', status=status.HTTP_400_BAD_REQUEST)
            messages.error(request, message)
            return HttpResponse(message, status=status.HTTP_400_BAD_REQUEST)
        else:
            return HttpResponse(str(exception), status=status.HTTP_400_BAD_REQUEST)
