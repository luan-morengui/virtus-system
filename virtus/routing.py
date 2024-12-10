from django.urls import path
from .consumers import PresencaConsumer

websocket_urlpatterns = [
    path('ws/presencas/', PresencaConsumer.as_asgi()),
]
