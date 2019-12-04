from ..baseService import BaseService
from ..logger import PyplanLogger
from pyplan.pyplan.common.redisService import RedisService
from django.utils.deprecation import MiddlewareMixin


class SessionMiddleware(MiddlewareMixin):

    def process_request(self, request):
        redis = RedisService()
        try:
            redis.set_active_session(request)
            srv = BaseService(request)
            PyplanLogger().logInfo(request, srv.client_session)
        except:
            pass

    def process_response(self, request, response):
        redis = RedisService()
        try:
            redis.del_active_session(request)
        except:
            pass
        return response

    def process_exception(self, request, exception):
        redis = RedisService()
        try:
            redis.del_active_session(request)
        except:
            pass
        try:
            print(f"process_exception: {str(exception)}")
            PyplanLogger().logError(request, str(exception))
        except:
            pass
