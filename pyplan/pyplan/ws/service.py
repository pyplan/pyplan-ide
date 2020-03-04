from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


def sysMsg(channel_name, msg_type, not_level, content={}):
    """
    Notify system message to channel
    """
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        channel_name,
        {
            'type': 'notify.system_message',
            'msg_type': msg_type,
            'not_level': not_level,
            **content
        },
    )
