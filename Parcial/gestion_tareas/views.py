from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('Esta es mi primera vista')

def Login(request):
    if request.method=='POST':
        print('Hola')
        nombre=request.POST.get('informacion')
        print(str(nombre))
    return render(request,'gestion_tareas/Login.html',{
        'nombre':'Pedro',
        'apellido':'Alegria',
        'edad':'25'
    })