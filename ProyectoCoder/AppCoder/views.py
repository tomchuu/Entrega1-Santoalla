from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import *
from AppCoder.forms import *
# Create your views here.

def inicio(request):
    
    return render(request, "AppCoder/inicio.html")



def gimnasio(request):
    
    return render(request, "AppCoder/gimnasio.html")




def cliente (request):
    
    return render(request, "AppCoder/cliente.html")



def rutinas(request):
    
    return render(request, "AppCoder/rutinas.html")


def formulario1(request):

    if request.method =="POST":

        formulario1 = FormularioRutinas(request.POST)

        if formulario1.is_valid():

            info = formulario1.cleaned_data

            rutinaF = Rutinas(nombre=info["nombre"], dias=info["dias"])

            rutinaF.save()

            return render(request, "AppCoder/inicio.html")


    else:

        formulario1=FormularioRutinas()

    
    return render(request, "AppCoder/formu1.html", {"form1":formulario1})



def formulario2(request):

    if request.method=="POST":

        formulario2 = FormularioCliente(request.POST)

        if formulario2.is_valid():

            info = formulario2.cleaned_data

            clienteF = Cliente(nombre=info["nombre"], apellido=info["apellido"], fechadeingreso=info["fechadeingreso"])

            clienteF.save()

            return render(request, "AppCoder/inicio.html")

    else:

        formulario2 = FormularioCliente()


    return render(request, "AppCoder/formu2.html", {"form2":formulario2})



def formulario3(request):

    if request.method=="POST":

        formulario3 = FormularioGimnasio(request.POST)

        if formulario3.is_valid():

            info = formulario3.cleaned_data

            gimnasioF = Gimnasio(nombre=info["nombre"], valoracion=info["valoracion"])

            gimnasioF.save()

            return render(request, "AppCoder/gimnasio.html")

    else:

        formulario3 = FormularioGimnasio()

    return render(request, "AppCoder/formu3.html", {"form3":formulario3})



def busquedaRutinas(request):

    return render(request, "AppCoder/busquedaRutinas.html")


def buscar(request):


    if request.GET["rutinas"]:
     
     busqueda = request.GET["rutinas"]
     rutinas = Rutinas.objects.filter(nombre__icontains=busqueda)
     
     return render(request, "AppCoder/resultados.html", {"rutinas":rutinas, "busqueda":busqueda} )

    else :
        
        mensaje = "No ingresaste datos."

  
    return HttpResponse(mensaje)