from json import dumps
from logging import getLogger
from os import getenv
from time import sleep

from threading import Thread
from websocket import WebSocketApp
from .ws_settings import ws_settings


PYPLAN_API_HOST = getenv(
    'PYPLAN_API_HOST', default='http://pyplanapi:8000/api')
WS_PROTOCOL = 'wss' if 'https' in PYPLAN_API_HOST else 'ws'
WS_URI = f'{WS_PROTOCOL}://{PYPLAN_API_HOST.split("://")[1]}/ws'

logger = getLogger('django')


class WS:
    def __init__(self, company_code: str, session_key: str):
        self.company_code = company_code
        self.session_key = session_key
        self.ws = self._start()

    def _start(self):
        socket_uri = f'{WS_URI}/notifications/{self.company_code}/?sessionKey={self.session_key}'
        ws = WebSocketApp(socket_uri, on_open=self._on_open,
                          on_error=self._on_error, on_close=self._on_close)

        def start_run(ws):
            ws.run_forever(ping_interval=10)
        th = Thread(target=start_run, args=(ws,))
        th.start()

        return ws

    def _on_open(self, ws):
        try:
            ws.send(dumps({
                    'command': 'join',
                    'room': self.session_key,
                    'message': 'Engine Joining!',
                    'company_code': self.company_code,
                    }))
        except Exception as ex:
            logger.error(f'Error in WebSocket join: {str(ex)}')

    def _ensure_ws(self):
        if self.ws is None or not self.ws.keep_running:
            self._start()
            nn = 0
            while nn < 10:
                if not self.ws is None and self.ws.keep_running:
                    break
                sleep(1)
                nn += 1

    def _on_close(self, ws):
        logger.error(f'WebSocket has closed')

    def _on_error(self, ws, error):
        logger.error(f'Error in WebSocket: {str(error)}')

    def sendMsg(self, message, title=None, not_level=None):
        try:
            self._ensure_ws()
            self.ws.send(dumps({
                'msg_type': ws_settings.MSG_TYPE_MESSAGE,
                'not_level': not_level if not not_level is None else ws_settings.NOTIFICATION_LEVEL_INFO,
                'command': 'send',
                'room': self.session_key,
                'company_code': self.company_code,
                'message': message,
                'title': title if not title is None else '',
            }))
        except Exception as ex:
            logger.error(f'Error in WebSocket sendMsg: {str(ex)}')

    def progressbar(self, progress, message=None):
        try:
            self._ensure_ws()
            self.ws.send(dumps({
                'msg_type': ws_settings.MSG_TYPE_PROGRESSBAR,
                'command': 'send',
                'room': self.session_key,
                'company_code': self.company_code,
                'progress': progress,
                'message': message if not message is None else ''
            }))
        except Exception as ex:
            logger.error(f'Error in WebSocket send: {str(ex)}')

    def sendDebugInfo(self, node, title, action, time=0, usedMemory=0, totalMemory=0, maxMemory=0, fromDynamic=False):
        try:
            self._ensure_ws()
            self.ws.send(dumps({
                'msg_type': ws_settings.MSG_TYPE_DEBUG_MODE_INFO,
                'command': 'send',
                'room': self.session_key,
                'company_code': self.company_code,
                'message': '',
                'node': node,
                'title': title,
                'action': action,
                'fromDynamic': fromDynamic,
                'time': time,
                'usedMemory': usedMemory,
                'totalMemory': totalMemory,
                'maxMemory': maxMemory
            }))
        except Exception as ex:
            logger.error(f'Error in WebSocket sendDebugInfo: {str(ex)}')
