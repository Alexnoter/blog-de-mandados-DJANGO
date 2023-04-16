from django.urls import path
from .views import ListaPendientes

#urls path no puede mostrar clases , el metodo es as_view() para que si pueda
urlpatterns = [path('', ListaPendientes.as_view(), name='pendientes')]
