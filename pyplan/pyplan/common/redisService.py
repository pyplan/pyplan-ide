import os
from json import dumps, loads

#import redis


class RedisService(object):

    def __init__(self):
        pass

    def _read_dic(self, key):
        return {}

    def _write_dic(self, key, dic):
        pass

    def get_running_tasks(self):
        """Return running tasks"""
        return []

    def set_running_tasks(self, tasks):
        """Set running task """
        pass

    def put_running_task(self, currentSession, engineURI, engineUID, engineParams):
        """put in redis current running task"""
        pass

    def del_running_task(self, currentSession):
        """put in redis current running task"""
        pass

    # Task id in execution

    def set_task_in_execution(self, task_id):
        """ Add task_id in execution """
        pass

    def del_task_in_execution(self, task_id):
        """ Remove task_id from execution """
        pass

    def is_task_in_execution(self, task_id):
        return False

    # active sessions

    def set_active_session(self, request):
        """Add session_key to active sessions"""
        pass

    def del_active_session(self, request):
        """Remove session_key from active sessions"""
        pass

    def is_active_session(self, session_key):
        """Return true if session_key is an active session"""
        return False

    def sessions_in_use(self):
        return []

    # saving models

    def set_saving_model(self, session_key):
        """ Add session_key to saving model (for prevent kill engines while is saving model"""
        pass

    def del_saving_model(self, session_key):
        """ Remove session_key from saving model"""
        pass

    def is_saving_model(self, session_key):
        """ Return true if session_key is saving model"""
        return False
