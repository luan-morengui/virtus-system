from django.shortcuts import render
from .models import UserInfo, Timesheet
from django.utils.timezone import now
import time 
from django.http import StreamingHttpResponse
from django.db import models
import json
from django.utils.timezone import localtime


# Create your views here.
def index(request):
    hoje = now().date()
    presencas = Timesheet.objects.filter(
        entrada__date=hoje,
        saida__isnull=True
    ).select_related('user__info')
    
   
    return render(request, 'index.html', {'presencas': presencas})


# Buffer para armazenar eventos de atualização
updates = []


def monitor_updates():
    """Generator que verifica novos registros ou atualizações no banco."""
    ultima_verificacao = localtime()
    
    while True:
        registros_atualizados = Timesheet.objects.filter(
            entrada__date=localtime().date(),
        ).filter(
            models.Q(entrada__gt=ultima_verificacao) | models.Q(saida__gt=ultima_verificacao)
        ).select_related('user__info')
        

        if registros_atualizados.exists():
            for registro in registros_atualizados:
                if registro.saida:  # Atualização de saída
                    yield f"data: {json.dumps({'action': 'exit', 'user': {'id': registro.user.id}})}\n\n"
                else:  # Nova entrada
                    user_info = registro.user.info
                    yield f"data: {json.dumps({'action': 'entry', 'user': {'id': registro.user.id, 'name': registro.user.get_full_name(), 'photo': f'data:image/jpeg;base64,{user_info.foto_base64}' if user_info.foto_base64 else 'https://via.placeholder.com/150', 'role': user_info.cargo, 'room': user_info.sala}})}\n\n"

            ultima_verificacao = localtime()

        time.sleep(2)  # Verifica a cada 5 segundos


def employee_presence_stream(request):
    """View que envia atualizações em tempo real."""
    response = StreamingHttpResponse(monitor_updates(), content_type="text/event-stream")
    response['Cache-Control'] = 'no-cache'
    return response