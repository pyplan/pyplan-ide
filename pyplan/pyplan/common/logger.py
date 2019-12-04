from datetime import datetime, timezone


class PyplanLogger():

    def logInfo(self, request, client_session=None, extra_info=None):
        pass

    def logError(self, request, ex):
        pass

    def logEndSession(self, request, client_session):
        pass
