from datetime import datetime

from channels.generic.websocket import AsyncJsonWebsocketConsumer

from .exceptions import ClientError
from .settings import ws_settings


class NotifyConsumer(AsyncJsonWebsocketConsumer):
    """
    This notify consumer handles websocket connections for clients notifications.
    It uses AsyncJsonWebsocketConsumer, which means all the handling functions
    must be async functions, and any sync work (like ORM access) has to be
    behind database_sync_to_async or sync_to_async. For more, read
    http://channels.readthedocs.io/en/latest/topics/consumers.html
    """

    # ### WebSocket event handlers

    async def connect(self):
        """
        Called when the websocket is handshaking as part of initial connection.
        """
        self.main_group = self.scope['url_route']['kwargs']['main_group']

        if self.scope['user'].is_anonymous:
            # Reject the connection
            await self.close()

        # Join main group
        await self.channel_layer.group_add(
            self.main_group,
            self.channel_name,
        )
        await self.accept()

        # Store which rooms the user has joined on this connection
        self.rooms = set()
        self.rooms.add(self.main_group)

    async def receive_json(self, content):
        """
        Called when we get a text frame. Channels will JSON-decode the payload
        for us and pass it as the first argument.
        """
        # Messages will have a 'command' key we can switch on
        command = content.get('command', None)
        try:
            if command == 'join':
                # Make them join the room
                await self.join_room(content['room'])
            elif command == 'leave':
                # Leave the room
                await self.leave_room(content['room'])
            elif command == 'send':
                await self.send_room(content)
        except ClientError as e:
            # Catch any errors and send it back
            await self.send_json({'error': e.code})

    async def disconnect(self, close_code):
        """
        Called when the WebSocket closes for any reason.
        """
        # Leave all the rooms we are still in
        for room_id in list(self.rooms):
            try:
                await self.leave_room(room_id)
            except ClientError:
                pass

    # ### Command helper methods called by receive_json

    async def join_room(self, room_id):
        """
        Called by receive_json when someone sent a join command.
        """
        # The logged-in user is in our scope thanks to the authentication ASGI middleware
        # room = await get_room_or_error(room_id, self.scope['user'])
        # Send a join message if it's turned on
        if ws_settings.NOTIFY_USERS_ON_ENTER_OR_LEAVE_ROOMS:
            await self.channel_layer.group_send(
                room_id,
                {
                    'type': 'chat.join',
                    'msg_type': ws_settings.MSG_TYPE_ENTER,
                    'room_id': room_id,
                    # 'username': self.scope['user'].username,
                }
            )
        # Store that we're in the room
        self.rooms.add(room_id)
        # Add them to the group so they get room messages
        await self.channel_layer.group_add(
            room_id,
            self.channel_name,
        )
        # Instruct their client to finish opening the room
        await self.send_json({
            'join': room_id,
            'title': 'joined %s' % room_id,
        })

    async def leave_room(self, room_id):
        """
        Called by receive_json when someone sent a leave command.
        """
        # The logged-in user is in our scope thanks to the authentication ASGI middleware
        # room = await get_room_or_error(room_id, self.scope['user'])
        # Send a leave message if it's turned on
        if ws_settings.NOTIFY_USERS_ON_ENTER_OR_LEAVE_ROOMS:
            await self.channel_layer.group_send(
                room_id,
                {
                    'type': 'chat.leave',
                    'msg_type': ws_settings.MSG_TYPE_LEAVE,
                    'room_id': room_id,
                    # 'username': self.scope['user'].username,
                }
            )
        # Remove that we're in the room
        self.rooms.discard(room_id)
        # Remove them from the group so they no longer get room messages
        await self.channel_layer.group_discard(
            room_id,
            self.channel_name,
        )
        # Instruct their client to finish closing the room
        await self.send_json({
            'leave': room_id,
        })

    async def send_room(self, content):
        """
        Called by receive_json when someone sends a message to a room.
        """

        room_id = content['room']
        msg_type = content['msg_type'] if 'msg_type' in content else ws_settings.MSG_TYPE_MESSAGE
        not_level = content['not_level'] if 'not_level' in content else ws_settings.NOTIFICATION_LEVEL_INFO

        payload = {}
        if msg_type == ws_settings.MSG_TYPE_MESSAGE:
            payload = {
                'type': 'chat.message',
                'msg_type': msg_type,
                'not_level': not_level,
                'message': content['message'],
                'title': content['title'] if 'title' in content else ''
            }
        elif msg_type == ws_settings.MSG_TYPE_PROGRESSBAR:
            payload = {
                'type': 'chat.message',
                'msg_type': msg_type,
                'not_level': not_level,
                'message': content['message'],
                'progress': content['progress'] if 'progress' in content else 0
            }
        elif msg_type == ws_settings.MSG_TYPE_DEBUG_MODE_INFO:
            payload = {
                'type': 'chat.message',
                'msg_type': msg_type,
                'not_level': not_level,
                'message': content['message'],
                'node': content['node'],
                'title': content['title'],
                'action': content['action'],
                'fromDynamic': content['fromDynamic'],
                'time': content['time'],
                'usedMemory': content['usedMemory'],
                'totalMemory': content['totalMemory']
            }

        # Check they are in this room
        # if room_id not in self.rooms:
        #     raise ClientError('ROOM_ACCESS_DENIED')
        # Get the room and send to the group about it
        # room = await get_room_or_error(room_id, self.scope['user'])
        await self.channel_layer.group_send(
            room_id,
            payload
        )

    # ### Handlers for messages sent over the channel layer

    # These helper methods are named by the types we send - so chat.join becomes chat_join
    async def chat_join(self, event):
        """
        Called when someone has joined our chat.
        """
        # Send a message down to the client
        await self.send_json(
            {
                'msg_type': ws_settings.MSG_TYPE_ENTER,
                'room': event['room_id'],
                # 'company_code': event['company_code'],
                # 'username': event['username'],
            },
        )

    async def chat_leave(self, event):
        """
        Called when someone has left our chat.
        """
        # Send a message down to the client
        await self.send_json(
            {
                'msg_type': ws_settings.MSG_TYPE_LEAVE,
                'room': event['room_id'],
                # 'company_code': event['company_code'],
                # 'username': event['username'],
            },
        )

    async def chat_message(self, event):
        """
        Called when someone has messaged our chat.
        """
        # Send a message down to the client
        event.update({'timestamp': str(datetime.now())})
        await self.send_json(event)

    async def notify_system_message(self, event):
        """
        Called when someone has messaged our chat.
        """
        # Send a message down to the client
        await self.send_json(
            {
                'msg_type': event['msg_type'],
                # 'msg_type': ws_settings.MSG_TYPE_MESSAGE,
                # 'room': event['room_id'],
                # 'username': event['username'],
                'title': event['title'] if 'title' in event else '',
                'message': event['message'] if 'message' in event else '',
                'not_level': event['not_level'],
                # 'not_type': ws_settings.MSG_TYPE_INFO,
                'timestamp': str(datetime.now()),
            },
        )
