class ws_settings:
    NOTIFY_USERS_ON_ENTER_OR_LEAVE_ROOMS = False

    # ### Message types
    MSG_TYPE_MESSAGE = 0  # For standard messages
    MSG_TYPE_SESSION_KILLED = 1  # For session killed messages
    MSG_TYPE_LEAVE = 2
    MSG_TYPE_ENTER = 3
    MSG_TYPE_PROGRESSBAR = 4  # For progressbar messages
    MSG_TYPE_OPENING_MODEL = 5  # For opening model progress

    MESSAGE_TYPES_CHOICES = (
        (MSG_TYPE_MESSAGE, 'MESSAGE'),
        (MSG_TYPE_SESSION_KILLED, 'SESSION_KILLED'),
        (MSG_TYPE_PROGRESSBAR, 'PROGRESSBAR'),
    )

    MESSAGE_TYPES_LIST = [
        MSG_TYPE_MESSAGE,
        MSG_TYPE_SESSION_KILLED,
        MSG_TYPE_PROGRESSBAR,
    ]

    # ### Notification Levels
    NOTIFICATION_LEVEL_INFO = 0
    NOTIFICATION_LEVEL_SUCCESS = 1
    NOTIFICATION_LEVEL_ERROR = 2

    NOTIFICATION_LEVEL_CHOICES = (
        (NOTIFICATION_LEVEL_INFO, 'info'),
        (NOTIFICATION_LEVEL_SUCCESS, 'success'),
        (NOTIFICATION_LEVEL_ERROR, 'error'),
    )
