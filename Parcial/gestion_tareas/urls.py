###archivo creado, línea añadida
from . import views
from django.urls import path

app_name='gestion_tareas'

urlpatterns=[
    path('',views.index, name='index'),
    path('Login',views.Login,name='Login')
]