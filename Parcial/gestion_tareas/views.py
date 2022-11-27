from django.shortcuts import render
from django.http import HttpResponse
from .models import Tarea
from .models import Usuario

#from django.shortcuts import redirect

# Create your views here.

def index(request):
    return HttpResponse('Esta es mi primera vista')

#Se tienen los siguientes usuarios guardados:
#[[NOMBRE1,APELLIDO1,ABC,CONABC],[NOMBRE2,APELLIDO2,DEF,CONDEF],[NOMBRE3,APELLIDO3,GHI,CONGHI]]
def Login(request):
    PAGINA=0
    if request.method=='POST':
        UsuarioMODELO=Usuario.objects.all().order_by('id')
        Nombre=request.POST.get('NombreUsuario')
        Clave=request.POST.get('ClaveUsuario')
        for ingreso in UsuarioMODELO:
            if ingreso.Nombre==Nombre and ingreso.Clave==Clave:
                PAGINA=1
                break
    if PAGINA==0:
        #return render(request,'gestion_tareas/Login.html',{'UsuarioMODELO':Tarea.objects.all().order_by('id'),})
        return render(request,'gestion_tareas/Login.html')
    else:
        #return render(request,'gestion_tareas/Dashboard.html',{'UsuarioMODELO':Tarea.objects.all().order_by('id'),})
            return render(request,'gestion_tareas/Dashboard.html',{
                'TareaMODELO':Tarea.objects.all().order_by('id'),
            })


def Dashboard(request):
    if request.method=='POST':
        Titulo=request.POST.get('TituloTarea')
        Descripcion=request.POST.get('DescripcionTarea')
        Fecha_de_creacion=request.POST.get('FechaCTarea')
        Fecha_de_entrega=request.POST.get('FechaETarea')
        Usuario_designado=request.POST.get('UsuarioTarea')
        Tarea(Titulo=str(Titulo),Descripcion=str(Descripcion),Fecha_de_creacion=str(Fecha_de_creacion),Fecha_de_entrega=str(Fecha_de_entrega),Usuario_designado=str(Usuario_designado)).save()
    return render(request,'gestion_tareas/Dashboard.html',{
        'TareaMODELO':Tarea.objects.all().order_by('id'),
    })

def Detalletareas(request,ind):
    tarea_seleccionada=Tarea.objects.get(id=ind)
    return render(request,'gestion_tareas/Detalletareas.html',{
        'tarea_seleccionada':tarea_seleccionada
    })