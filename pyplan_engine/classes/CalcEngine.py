import multiprocessing
import os
import re
import time
import uuid
from multiprocessing.managers import BaseManager
from sys import platform
from threading import Timer

from pyplan_engine.ws.ws import WS
from pyplan_core.classes.Model import Model


class ProcessManager(BaseManager):
    pass


ProcessManager.register('Model', Model)


class CalcEngine(object):

    def __init__(self, mode=None, resources=None):
        self._manager = None
        self._uid = uuid.uuid4().hex
        self._pid = 0
        self._model = None
        self.stoppable = False
        self.forced_stopped = False
        self.stop_reason = ""
        self.stopping = False
        self.mode = mode if mode else "fixed"
        self.resources = resources
        self.maxMemoryForSession = 8
        if os.getenv('MAX_MEMORY_FOR_SESSION', '32'):
            self.maxMemoryForSession = int(
                os.getenv('MAX_MEMORY_FOR_SESSION', '32'))

    def initializeModel(self, modeFileName=None, skipStartMonitor=False):
        self._model = Model(WS)
        self._pid = self._model.getPID()
        # unsupported multiprocess for pyplan-ide
        # if os.getenv('USE_MULTIPROCESS', '0') == "1":

        #     self._manager = ProcessManager()
        #     self._manager.start()
        #     self._model = self._manager.Model(WS)
        #     self._pid = self._model.getPID()
        #     if self.resources and "mem_limit" in self.resources and self.resources["mem_limit"]:
        #         self.maxMemoryForSession = float(re.findall(
        #             r'\d+', self.resources["mem_limit"])[0])
        # else:
        #     self._model = Model(WS)
        #     self._pid = self._model.getPID()

    @property
    def uid(self):
        return self._uid

    @property
    def pid(self):
        return self._pid

    @property
    def model(self):
        if self._model is None:
            self.initializeModel()
        return self._model

    @property
    def isMultiprocess(self):
        return False if self._manager is None else True

    def isAlive(self):
        return False if self._model is None else True

    def getStopReason(self):
        return self.stop_reason

    def stop(self, reason="Stopped by user"):
        import sys

        try:
            if not self.stopping and self.isMultiprocess and self.stoppable:
                self.stopping = True
                current_model_path = self._model.getCurrentModelPath()
                _tmp_ppl = self._model.saveModel()
                self.stop_reason = reason
                self._manager.shutdown()
                self._manager = None
                self._model = None
                self.initializeModel(os.path.join(
                    current_model_path, "dummy.ppl"), True)
                self._model.openModel(os.path.join(
                    current_model_path, "dummy.ppl"), textModel=_tmp_ppl)
                self._model.setCurrentModelPath(current_model_path)
                self.stoppable = False
                self.stop_reason = ""
        except Exception as ex:
            print(f"Stop error: {str(ex)}")
        finally:
            self.stopping = False

    def release(self):
        self.mode = None
        self.resources = None
        if not self.model is None:
            try:
                self.model.release()
            except Exception as ex:
                pass
            if not self._manager is None:
                self._manager.shutdown()
                self._manager = None
            self._model = None
