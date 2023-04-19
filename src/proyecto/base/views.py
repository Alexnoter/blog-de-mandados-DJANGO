from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Tarea



# Create your views here.


#listaview requiere 2 cosas un model y un qriser
class ListaPendientes(ListView):
    model = Tarea
    context_object_name = 'tareas'

class DetalleTarea(DetailView):
    model = Tarea
    context_object_name = 'tarea'
    template_name = 'base/tarea.html' # con esto decimos que me reconosca que ahora sera tarea.html y no tarea_detail


