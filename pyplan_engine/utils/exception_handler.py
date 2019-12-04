import traceback

from django.conf import settings
from django.http import HttpResponse
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.views import exception_handler


def genericApiException(ex, engine=None):

    msg = "No error data"
    if not engine is None and engine.getStopReason():
        msg = engine.getStopReason()
    else:
        if not ex is None:
            msg = str(ex.args)
        if settings.DEBUG:
            msg += "\n----------------\n" + traceback.format_exc()

    return HttpResponse(msg, content_type="text/plain", status=207)


def ex_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    #response = exception_handler(exc, context)

    msg = "Unmanaged error."
    if not exc is None:
        msg += " "+str(exc.args[0])

    if settings.DEBUG:
        msg += "\n----------------\n" + traceback.format_exc()

    return HttpResponse(msg, content_type="text/plain", status=207)
