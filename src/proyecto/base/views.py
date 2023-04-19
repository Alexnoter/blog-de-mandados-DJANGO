from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
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


class CrearTarea(CreateView):
    model = Tarea
    fields = '__all__' #con esto cargamos todos los datos del formulario de los modelos todos los datos otra manera de cargar es []
    success_url = reverse_lazy('tareas')


class EditarTarea(UpdateView):
    model = Tarea
    fields = '__all__'
    success_url = reverse_lazy('tareas')


