# models.py
from django.db import models

class Medico(models.Model):
    nome = models.CharField(max_length=255)
    especialidade = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Paciente(models.Model):
    nome = models.CharField(max_length=255)
    plano = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class MarcarConsulta(models.Model):
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    dia = models.DateField()
    horario = models.TimeField()

    def __str__(self):
        return f"{self.medico} - {self.paciente} - {self.dia} - {self.horario}"
