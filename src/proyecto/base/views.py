from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin   #restingir , estableces que clase de usuario sera
from django.urls import reverse_lazy
from .models import Tarea



# Create your views here.

class Logueo(LoginView):
    template_name = 'base/login.html'
    field = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tareas')


#listaview requiere 2 cosas un model y un qriser
class ListaPendientes(LoginRequiredMixin, ListView):
    model = Tarea
    context_object_name = 'tareas'

class DetalleTarea(LoginRequiredMixin, DetailView):
    model = Tarea
    context_object_name = 'tarea'
    template_name = 'base/tarea.html' # con esto decimos que me reconosca que ahora sera tarea.html y no tarea_detail


class CrearTarea(LoginRequiredMixin, CreateView):
    model = Tarea
    fields = '__all__' #con esto cargamos todos los datos del formulario de los modelos todos los datos otra manera de cargar es []
    success_url = reverse_lazy('tareas')


class EditarTarea(LoginRequiredMixin, UpdateView):
    model = Tarea
    fields = '__all__'
    success_url = reverse_lazy('tareas')


class EliminarTarea(LoginRequiredMixin, DeleteView):
    model = Tarea
    context_object_name = 'tarea'
    success_url = reverse_lazy('tareas')


