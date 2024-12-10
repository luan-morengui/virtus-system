from django.urls import path ,include
from virtus import views


urlpatterns = [
    path('', views.index, name='index'), 
    path('stream/', views.employee_presence_stream, name='employee_presence_stream'),
]