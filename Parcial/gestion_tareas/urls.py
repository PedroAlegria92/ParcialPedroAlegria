###archivo creado, línea añadida
from . import views
from django.urls import path

app_name='gestion_tareas'

urlpatterns=[
    path('',views.index, name='index'),
    path('Login',views.Login,name='Login'),
    path('Dashboard',views.Dashboard,name='Dashboard'),
    path('Detalletareas/<str:ind>',views.Detalletareas,name='Detalletareas'),
    path('eliminarTarea/<str:ind>',views.eliminarTarea,name='eliminarTarea')
]