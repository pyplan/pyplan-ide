class ws_settings:
    MSG_TYPE_MESSAGE = 0  # For standard messages
    MSG_TYPE_SESSION_KILLED = 1  # For session killed messages
    MSG_TYPE_LEAVE = 2
    MSG_TYPE_ENTER = 3
    MSG_TYPE_PROGRESSBAR = 4  # For progressbar messages
    MSG_TYPE_DEBUG_MODE_INFO = 6  # For debug mode messages

    # ### Notification Levels
    NOTIFICATION_LEVEL_INFO = 0
    NOTIFICATION_LEVEL_SUCCESS = 1
    NOTIFICATION_LEVEL_ERROR = 2
    NOTIFICATION_LEVEL_WARNING = 3

    NOTIFICATION_LEVEL_CHOICES = (
        (NOTIFICATION_LEVEL_INFO, 'info'),
        (NOTIFICATION_LEVEL_SUCCESS, 'success'),
        (NOTIFICATION_LEVEL_ERROR, 'error'),
        (NOTIFICATION_LEVEL_WARNING, 'warning'),
    )
