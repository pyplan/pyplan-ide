import os

from rest_framework import exceptions


class EngineManager(object):
    """ Class to create engine manager to manage engine endpoints. This work in 3 modes:
        mode fixed: only one URI, multiples UID
        mode docker api: call to docker api to create new container for each session
        mode aws: call to aws api (to confirm)
    """

    @staticmethod
    def createManager():
        return None
