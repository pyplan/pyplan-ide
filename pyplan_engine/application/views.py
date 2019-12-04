import os

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from pyplan_engine.classes.Application import Application
from pyplan_engine.utils.exception_handler import genericApiException


@api_view(["GET"])
def test(request):
    try:
        return JsonResponse({"app": "OK"}, safe=False)
    except Exception as e:
        return genericApiException(e)


@api_view(["GET"])
def getStatus(request):
    """GET app status"""
    try:
        app = Application()
        return JsonResponse(app.getStatus(), safe=False)
    except Exception as e:
        return genericApiException(e)


@api_view(["GET"])
def sleep(request):
    """ Try sleep 10 seconds
    """
    try:
        import time
        time.sleep(10)
        return JsonResponse({"sleep": "OK"}, safe=False)
    except ValueError as e:
        return genericApiException(e)


@api_view(["GET"])
def checkRead(request):
    """Check read"""
    try:
        _path = request.query_params.get("path")
        import os
        res = str(os.listdir(_path))
        return HttpResponse(res)
    except ValueError as e:
        return genericApiException(e)


@api_view(["GET"])
def checkWrite(request):
    """Check write"""
    try:
        _path = request.query_params.get("path")
        import os
        _file = open(_path + "test.txt", "w")
        _file.write("engine write test")
        _file.close()

        return HttpResponse(_path + "test.txt")
    except ValueError as e:
        return genericApiException(e)


@api_view(["GET"])
def healthCheck(request, *args, **kargs):
    return Response(status=status.HTTP_200_OK)


@api_view(["GET"])
def cmdtest(request, *args, **kargs):
    _cmd = request.query_params.get("cmd")
    _list = str(_cmd).split(",")
    import subprocess

    p = subprocess.Popen(_list, stdout=subprocess.PIPE)
    out = p.stdout.read()
    out = str(out).replace("\\n", "<br>")
    return HttpResponse(out)
