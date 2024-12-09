from django.urls import path ,include
from virtus import views


urlpatterns = [
    path('', views.index, name='index'), 
]