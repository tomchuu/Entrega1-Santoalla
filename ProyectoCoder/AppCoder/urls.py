
from django.urls import path
from AppCoder.views import *
urlpatterns = [
    path("", inicio, name="Inicio"),
    path("gimnasio", gimnasio, name="Gimnasio"),
    path("cliente", cliente, name="Cliente"),
    path("rutinas", rutinas, name="Rutinas"),
    path("form1/", formulario1),
    path("form2/", formulario2),
    path("form3/", formulario3),
    path("buscarRutinas/", busquedaRutinas),
    path("buscar/", buscar),
]