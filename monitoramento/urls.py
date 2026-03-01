from django.urls import path
from . import views

urlpatterns = [
    path('', views.monitoramento, name="home")
]