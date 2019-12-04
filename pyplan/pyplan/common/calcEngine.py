import json
import os
import requests
from django.contrib.sessions.models import Session
from rest_framework import exceptions
from django.conf import settings

from pyplan.pyplan.app_pool.models import AppPool
from pyplan.pyplan.common.classes.eNodeProperty import eNodeProperty
from pyplan.pyplan.common.engineManager import EngineManager
from pyplan.pyplan.common.redisService import RedisService
from pyplan.pyplan.modelmanager.serializers.ModelInfoSerializer import (
    ModelInfo, ModelInfoSerializer)

from pyplan.pyplan.common.engineTypes.desktopType import DesktopType


class CalcEngine(object):

    @staticmethod
    def tryLoadFromAppPool(client_session, file):
        calc_engine = CalcEngine.factory(client_session)
        calc_engine.openModel(os.path.join(
            settings.MEDIA_ROOT, "models", file))
        return calc_engine

    @staticmethod
    def factory(clientSession):
        return DesktopType(clientSession)
