from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path, reverse_lazy
from django.views.generic.base import RedirectView
from rest_framework.authtoken import views
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import url

from channels.routing import ProtocolTypeRouter, URLRouter
from pyplan.pyplan.auth.views import (CustomAuthToken, PasswordReset,
                                      SendPasswordResetEmail)
from pyplan.pyplan.frontend.views import catchall as frontend_index
from pyplan.pyplan.ws.routing import websocket_urlpatterns
from pyplan.pyplan.ws.token_auth import TokenAuthMiddleware

application = ProtocolTypeRouter({
    'websocket': TokenAuthMiddleware(
        URLRouter(
            websocket_urlpatterns
        )
    ),
})

urlpatterns = [
    # Core
    path('api/admin/', admin.site.urls),

    path('api/token-auth/', CustomAuthToken.as_view()),
    path('api/sendPasswordResetEmail/', SendPasswordResetEmail.as_view()),
    path('api/passwordReset/', PasswordReset.as_view()),

    path('api/auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/doc/', include_docs_urls(
        title='Pyplan API',
        description="A description of how to use the API's...",
        authentication_classes=[],
        permission_classes=[]
    )),
    # API
    path('api/', include('pyplan.pyplan.urls')),

    re_path(r'', frontend_index),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
