import jsonpickle
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from pyplan_engine.classes.CalcEngine import CalcEngine
from pyplan_engine.engines import engines
from pyplan_engine.utils.exception_handler import genericApiException


@api_view(['POST', 'GET'])
def createEngine(request):
    """Create a new calc engine"""
    try:
        mode = request.data.get('mode')
        resources = request.data.get('engine_resources')
        print(resources)
        if resources:
            resources = jsonpickle.decode(resources)
        newEngine = CalcEngine(mode, resources)
        uid = newEngine.uid
        engines[uid] = newEngine
        newEngine = None
        return HttpResponse(uid)
    except Exception as e:
        return genericApiException(e)


@api_view(['POST', 'GET'])
def release(request, uid):
    """Release a calc engine"""
    try:
        if uid in engines:
            engines[uid].release()
            del engines[uid]
        return HttpResponse("ok")
    except Exception as e:
        return genericApiException(e)


@api_view(['POST'])
def stop(request, uid):
    """Stop process"""
    try:
        if uid in engines:
            res = engines[uid].stop()
            return HttpResponse(res)
    except Exception as e:
        return genericApiException(e)


@api_view(['POST', 'GET'])
def getpid(request, uid):
    """Return the PID of the uid engine"""
    try:
        if uid in engines:
            return HttpResponse(engines[uid].pid)
        else:
            return ""
    except Exception as e:
        return genericApiException(e)
