# admin.py
from django.contrib import admin
from .models import MarcarConsulta, Medico, Paciente

class MedicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'especialidade')
    search_fields = ('nome', 'especialidade')

class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'plano')
    search_fields = ('nome', 'plano')

class MarcarConsultaAdmin(admin.ModelAdmin):
    list_display = ('medico', 'paciente', 'dia', 'horario')
    search_fields = ('medico__nome', 'paciente__nome')
    list_filter = ('dia', 'medico')
    ordering = ('dia', 'horario')
    list_per_page = 10

admin.site.register(Medico, MedicoAdmin)
admin.site.register(Paciente, PacienteAdmin)
admin.site.register(MarcarConsulta, MarcarConsultaAdmin)
