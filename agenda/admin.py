from django.contrib import admin
from .models import Consulta
from .models import Data
from .models import Usuario

admin.site.register(Consulta)
admin.site.register(Usuario)

class consultaAdm(admin.ModelAdmin):
    fields = ['data', 'horario', 'medico', 'paciente', 'plano']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "paciente":
            kwargs["required"] = False
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    

admin.site.register(Data, consultaAdm)