from django.urls import path
from . import views

app_name="pruebas"

urlpatterns = [
    path('', views.home, name="home"),
    path('enviar_lista/', views.enviar_lista, name="enviar_lista" )
]