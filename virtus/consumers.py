from channels.generic.websocket import AsyncWebsocketConsumer
import json

class PresencaConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("presencas", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("presencas", self.channel_name)

    async def enviar_atualizacao(self, event):
        message = event["message"]
        await self.send(text_data=json.dumps({
            "message": message
        }))
