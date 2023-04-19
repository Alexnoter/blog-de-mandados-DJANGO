from django.urls import path
from .views import ListaPendientes, DetalleTarea, CrearTarea, EditarTarea

#urls path no puede mostrar clases , el metodo es as_view() para que si pueda
urlpatterns = [path('', ListaPendientes.as_view(), name='tareas'),
               path('tarea/<int:pk>', DetalleTarea.as_view(), name='tarea'),
               path('crear-tarea/', CrearTarea.as_view(), name='crear-tarea'),
               path('editar-tarea/<int:pk>', EditarTarea.as_view(), name='editar-tarea')]
