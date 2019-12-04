#from pyplan_engine.MainApp  import engines
import os
import time

from pyplan_engine.engines import engines


class Application(object):

    def __init__(self):
        pass

    def getStatus(self):
        """GET app status"""
        keys = [x for x in engines]
        res = {
            "useMultiprocess": (os.getenv('USE_MULTIPROCESS', '1') == "1"),
            "totalEngines": len(keys),
            "totalMemory": 0,
            "engines": []
        }
        for key in keys:
            item = {
                "key": key,
                "memory": engines[key].model.getTotalMemory(),
                "maxMemoryForSession": engines[key].maxMemoryForSession,
                "mode": engines[key].mode,
                "resources": engines[key].resources,
                "pid": engines[key].pid
            }
            res["totalMemory"] += engines[key].model.getTotalMemory()
            res["engines"].append(item)
        return res
