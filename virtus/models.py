from django.db import models
from django.contrib.auth.models import User, AbstractUser
from datetime import timedelta


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='info')
    foto_base64 = models.TextField(blank=True, null=True)  # Campo para armazenar a foto em Base64
    cargo = models.CharField(max_length=255, blank=True, null=True)  # Campo para o cargo da pessoa
    sala = models.CharField(max_length=50, blank=True, null=True)  # Campo para a sala da pessoa
    cartao_id = models.CharField(max_length=50, unique=True, blank=True, null=True)  # ID único do cartão NFC
    phone = models.CharField(max_length=50, blank=True, null=True)  # Telefone

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.cargo} - {self.sala}"

class Timesheet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='timesheets')
    entrada = models.DateTimeField(null=True, blank=True)  # Data e hora de entrada
    saida = models.DateTimeField(null=True, blank=True)    # Data e hora de saída

    
    def __str__(self):
        return f"{self.user.username} - Entrada: {self.entrada}, Saída: {self.saida}"
