from django.urls import path
from .views import ListaPendientes, DetalleTarea, CrearTarea, EditarTarea, EliminarTarea, Logueo
from django.contrib.auth.views import LogoutView

#urls path no puede mostrar clases , el metodo es as_view() para que si pueda
urlpatterns = [path('', ListaPendientes.as_view(), name='tareas'),
               path('login/', Logueo.as_view(), name='login'),
               path('logout/', LogoutView.as_view(next_page='login'), name='logout'), #ese next es para direccionar
               path('tarea/<int:pk>', DetalleTarea.as_view(), name='tarea'),
               path('crear-tarea/', CrearTarea.as_view(), name='crear-tarea'),
               path('editar-tarea/<int:pk>', EditarTarea.as_view(), name='editar-tarea'),
               path('eliminar-tarea/<int:pk>', EliminarTarea.as_view(), name='eliminar-tarea')]
