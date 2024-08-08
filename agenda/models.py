from django.db import models

class Consulta(models.Model):
    nomeMedico = models.CharField(max_length=255)
    especialidade = models.CharField(max_length=255)

class Usuario(models.Model):
    email = models.CharField(max_length=255)
    senha = models.CharField(max_length=255)
    administrador = models.BooleanField()

class Data(models.Model):
    dia = models.DateField()
    plano = models.BooleanField()
    medico = models.FloatField()
    paciente = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True,  default=None)