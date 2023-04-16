from django.contrib import admin
from .models import Tarea



# Register your models here.

#con esto hacemos que se visualice nuestra App de tarea en pantalla
admin.site.register(Tarea)
