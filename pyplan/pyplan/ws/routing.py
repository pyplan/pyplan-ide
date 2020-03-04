from django.conf.urls import url

from . import consumers

websocket_urlpatterns = [
    url(r'^api/ws/notifications/(?P<main_group>[^/]+)/$', consumers.NotifyConsumer),
]
