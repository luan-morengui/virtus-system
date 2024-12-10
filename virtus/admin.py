from django.contrib import admin
from .models import Timesheet, UserInfo
import base64
from django.utils.html import format_html
from django import forms


class UserInfoAdminForm(forms.ModelForm):
    # Adiciona um campo para upload de imagens
    foto_upload = forms.ImageField(required=False, label="Upload de Foto")

    class Meta:
        model = UserInfo
        fields = ['user', 'cargo', 'sala','cartao_id', 'foto_base64']  # Campos existentes no modelo

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.cleaned_data.get('foto_upload'):
            # Converte a imagem para Base64
            uploaded_image = self.cleaned_data['foto_upload']
            instance.foto_base64 = base64.b64encode(uploaded_image.read()).decode('utf-8')
        if commit:
            instance.save()
        return instance


@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    form = UserInfoAdminForm  # Usa o formulário personalizado
    list_display = ('user', 'cargo', 'sala', 'cartao_id','foto_preview')
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'cargo', 'sala')
    readonly_fields = ('foto_base64',)

    def foto_preview(self, obj):
        """Exibe uma prévia da foto no Django Admin."""
        if obj.foto_base64:
            return format_html(f'<img src="data:image/jpeg;base64,{obj.foto_base64}" width="50" height="50" />')
        return "Sem foto"
    foto_preview.short_description = "Foto"


# Register your models here.
@admin.register(Timesheet)
class TimesheetAdmin(admin.ModelAdmin):
    list_display = ('user', 'entrada', 'saida')
    list_filter = ('entrada', 'saida')