from django.shortcuts import render
from django.http import HttpResponse
from .models import Tarea

# Create your views here.

def index(request):
    return HttpResponse('Esta es mi primera vista')

def Login(request):
    if request.method=='POST':
        print('Hola')
        Titulo=request.POST.get('TituloTarea')
        Descripcion=request.POST.get('DescripcionTarea')
        Fecha_de_creacion=request.POST.get('FechaCTarea')
        Fecha_de_entrega=request.POST.get('FechaETarea')
        Usuario_designado=request.POST.get('UsuarioTarea')
        Tarea(Titulo=str(Titulo),Descripcion=str(Descripcion),Fecha_de_creacion=str(Fecha_de_creacion),Fecha_de_entrega=str(Fecha_de_entrega),Usuario_designado=str(Usuario_designado)).save()
    return render(request,'gestion_tareas/Login.html',{
        'TareaMODELO':Tarea.objects.all().order_by('id'),
    })