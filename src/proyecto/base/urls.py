from django.urls import path
from .views import ListaPendientes, DetalleTarea

#urls path no puede mostrar clases , el metodo es as_view() para que si pueda
urlpatterns = [path('', ListaPendientes.as_view(), name='pendientes'),
               path('tarea/<int:pk>', DetalleTarea.as_view(), name='tarea')]
