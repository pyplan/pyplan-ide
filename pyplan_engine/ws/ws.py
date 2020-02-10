import asyncio
from asyncio.futures import TimeoutError as ConnectionTimeoutError
from json import dumps
from logging import getLogger
from os import getenv

from websockets import connect as WSConnect

PYPLAN_API_HOST = getenv(
    'PYPLAN_API_HOST', default='http://pyplanapi:8000/api')
WS_PROTOCOL = 'wss' if 'https' in PYPLAN_API_HOST else 'ws'
WS_URI = f'{WS_PROTOCOL}://{PYPLAN_API_HOST.split("://")[1]}/ws'

logger = getLogger('django')


class WS:
    def __init__(self, ws=None, company_code=None, session_key=None):
        self.ws = ws
        self.company_code = company_code
        self.session_key = session_key

    @staticmethod
    def connect(company_code: str, session_key: str):
        async def _connect():
            ws = await WSConnect(f'{WS_URI}/notifications/{company_code}/?sessionKey={session_key}')
            await ws.send(dumps({
                'command': 'join',
                'room': session_key,
                'message': 'Engine Joining!',
                'company_code': company_code,
            }))
            return WS(ws, company_code, session_key)
        try:
            return asyncio.get_event_loop().run_until_complete(_connect())
        except ConnectionTimeoutError as ex:
            logger.error(
                f'Connection Timeout Error in WebSocket connect: {str(ex)}')
            return WS()
        except Exception as ex:
            logger.error(f'Error in WebSocket connect: {str(ex)}')
            return WS()

    def sendMsg(self, message=''):
        async def _sendMsg():
            return await self.ws.send(dumps({
                'command': 'send',
                'room': self.session_key,
                'type': 0,
                'session_key': self.session_key,
                'message': message,
            }))
        try:
            if self.ws is None or self.ws.closed:
                logger.error('WebSocket client is not stablished.')
            return asyncio.get_event_loop().run_until_complete(_sendMsg())
        except ConnectionTimeoutError as ex:
            logger.error(
                f'Connection Timeout Error in WebSocket sendMsg: {str(ex)}')
        except Exception as ex:
            logger.error(f'Error in WebSocket sendMsg: {str(ex)}')
