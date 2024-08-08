from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('agenda.urls')),  # Inclui as URLs do aplicativo 'agenda'
    path('admin/', admin.site.urls),   # URL para o painel de administração do Django
    path('auth/', include('django.contrib.auth.urls')),  # Inclui URLs de autenticação
]