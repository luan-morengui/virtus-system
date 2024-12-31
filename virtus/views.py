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
   
    return render(request, 'index.html')

def getPresencas(request):
    presencas = Timesheet.objects.filter(
        saida__isnull=True
    ).select_related('user__info')


    return render(request, 'partials/presencas.html', {'presencas': presencas})