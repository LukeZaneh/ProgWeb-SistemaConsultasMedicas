from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Data
from .models import Consulta

def consultas(request):
    return HttpResponse("Aqui estão as consultas.")

def home(request):
    template = loader.get_template('home.html')
    context = {
        "nome": "Centro médico PW"
    }
    return HttpResponse(template.render(context, request))

def administrador(request):
    template = loader.get_template('administrador.html')
    context = {
        'data': Data.objects.all().values(),
        'consultas': Consulta.objects.all().values()
    }
    return HttpResponse(template.render(context, request))

def data(request, id):    
    data = Data.objects.get(id=id)
    template = loader.get_template('data.html')
    context = {
        'data': data,
    }
    return HttpResponse(template.render(context, request))

def criarData(request):    
    return render(request, 'criarData.html')

def consulta(request, id):    
    consultas = Consulta.objects.get(id=id)
    template = loader.get_template('consultas.html')
    context = {
        'consultas': consultas,
    }
    return HttpResponse(template.render(context, request))

def criarConsulta(request):    
    return render(request, 'criarConsulta.html')

def cadastroConsulta(request):
    if request.method == "GET":
        return render(request, 'criarConsulta.html')
    else:
        data = request.POST.get('data')
        horario = request.POST.get('horario')
        plano = request.POST.get('plano')
        paciente = request.POST.get('paciente')

        novaConsulta = Consulta()
        novaConsulta.data = data
        novaConsulta.horario = horario
        novaConsulta.plano = plano
        novaConsulta.paciente = paciente 
        novaConsulta.save()

        template = loader.get_template('administrador.html')
        context = {
            'datas': Data.objects.all().values(),
            'consulta': Consulta.objects.all().values()
        }
        return HttpResponse(template.render(context, request))
    
def cadastroData(request):
    if request.method == "GET":
        return render(request, 'criarData.html')
    else:
        dia = request.POST.get('dia')
        horario = request.POST.get('horario')
        medico = request.POST.get('medico')
        plano = request.POST.get('plano')

        data = Data.objects.filter(dia=dia).first()
        hora = Data.objects.filter(horario=horario).first()
        medico = Data.objects.filter(medico=medico).first()
        if data & hora & medico:
            return HttpResponse('O horário de consulta já foi cadastrado para esse médico!')

        novaDataConsulta = Data()
        novaDataConsulta.dia = dia
        novaDataConsulta.horario = horario
        novaDataConsulta.medico = medico
        novaDataConsulta.planoSaude = plano
        novaDataConsulta.save()

        template = loader.get_template('administrador.html')
        context = {
            'datas': Data.objects.all().values(),
            'consulta': Consulta.objects.all().values()
        }
        return HttpResponse(template.render(context, request))
    
def alteraData(request):
    if request.method == "GET":
        template = loader.get_template('administrador.html')
        context = {
            'datas': Data.objects.all().values(),
            'consulta': Consulta.objects.all().values()
        }
        return HttpResponse(template.render(context, request))
    else:
        id = request.POST.get('id')
        data = request.POST.get('data')
        horario = request.POST.get('horario')
        medico = request.POST.get('medico')
        plano = request.POST.get('plano')
        dataDisponivel = Data.objects.filter(id=id).first()

        if dataDisponivel:
            dataDisponivel.data = data
            dataDisponivel.horario = horario
            dataDisponivel.medico = medico
            dataDisponivel.planoSaude = plano
            dataDisponivel.save()

            template = loader.get_template('administrador.html')
            context = {
            'datas': Data.objects.all().values(),
            'consulta': Consulta.objects.all().values()
            }
            return HttpResponse(template.render(context, request))
        else:
            return HttpResponse('O médico não possui disponibilidade nesse dia e horário!')