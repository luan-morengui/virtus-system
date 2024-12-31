from django.urls import path ,include
from virtus import views


urlpatterns = [
    path('', views.index, name='index'), 
    path('atualizar-presencas', views.getPresencas, name='atualizar-presencas'), 
]