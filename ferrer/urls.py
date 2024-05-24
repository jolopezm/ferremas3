from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('datos/', views.obtener_datos_banco_central, name='datos_banco_central'),
]