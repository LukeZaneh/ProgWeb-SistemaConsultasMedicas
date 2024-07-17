from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.principal, name='principal'),
    path('admin/', admin.site.urls), # definição da rota do ambiente adminstrativo
    path('marcarConsulta', views.marcar_consulta, name='marcarConsulta'),
    path('consultas', views.consultas, name='consultas'),
    path('detalhesConsulta/<int:id>', views.consulta_detalhes, name='detalhesConsulta'),
]
