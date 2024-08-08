from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # URL raiz do aplicativo
    path('app/administrador/', views.administrador, name='administrador'),
    path('app/administrador/data/<int:id>/', views.data, name='data'),
    path('app/administrador/data/criar/', views.criarData, name='criarData'),
    path('app/administrador/consulta/<int:id>/', views.consulta, name='consulta'),
    path('app/administrador/consulta/criar/', views.criarConsulta, name='criarConsulta'),
    path('cadastroConsulta/', views.cadastroConsulta, name='cadastroConsulta'),
    path('cadastroData/', views.cadastroData, name='cadastroData'),
    path('alteraData/', views.alteraData, name='alteraData'),
    path('app/consultas/', views.consultas, name='consultas'),  # Adicione a URL para consultas
]
