from django.urls import path
from . import views

urlpatterns = [
    path('', views.principal, name='principal'),
    path('marcarConsulta', views.marcar_consulta, name='marcarConsulta'),
    path('consultas', views.consultas, name='consultas'),
    path('detalhesConsulta/<int:id>', views.consulta_detalhes, name='detalhesConsulta'),
]
