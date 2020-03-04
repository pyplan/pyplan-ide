import os

import requests
from django.conf import settings
from rest_framework import exceptions

from pyplan.pyplan.common.engineTypes.desktopType import DesktopType


class CalcEngine(object):

    @staticmethod
    def tryLoadFromAppPool(client_session, file):
        calc_engine = CalcEngine.factory(client_session)
        calc_engine.openModel(os.path.join(settings.MEDIA_ROOT, 'models', file))
        return calc_engine

    @staticmethod
    def factory(clientSession):
        return DesktopType(clientSession)
