from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Tarea



# Create your views here.


#listaview requiere 2 cosas un model y un qriser
class ListaPendientes(ListView):
    model = Tarea
    context_object_name = 'tareas'
