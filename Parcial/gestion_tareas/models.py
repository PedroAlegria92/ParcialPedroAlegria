from django.db import models

# Create your models here.

class Tarea(models.Model):
    Titulo=models.CharField(max_length=64,default='')
    Descripcion=models.CharField(max_length=512,default='')
    Fecha_de_creacion=models.CharField(max_length=32,default='')
    Fecha_de_entrega=models.CharField(max_length=32,default='')
    Usuario_designado=models.CharField(max_length=64,default='')

class Usuario(models.Model):
    Nombre=models.CharField(max_length=64,default='')
    Apellido=models.CharField(max_length=64,default='')
    Codigo_de_usuario=models.CharField(max_length=32,default='')
    Clave=models.CharField(max_length=32,default='')