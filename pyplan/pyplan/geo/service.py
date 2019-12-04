from rest_framework import exceptions
from pyplan.pyplan.common.baseService import BaseService
from pyplan.pyplan.common.calcEngine import CalcEngine

class GeoService(BaseService):

    def getGeoData(self, query):
        """
        Return geoData result of node
        """
        if query.isCluster:
            return self.getClusterData(query)
        else:
            return self.getAllGeoData(query)

    def getClusterData(self):
        raise exceptions.NotAcceptable("Not yet implemented")

    def getAllGeoData(self, query):
        calcEngine = CalcEngine.factory(self.client_session)
        return calcEngine.getUnclusterData(query)
