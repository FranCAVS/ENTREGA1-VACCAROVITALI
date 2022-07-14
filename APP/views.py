from distutils.log import info
from enum import auto
from multiprocessing import context
from django import http
from django.shortcuts import render
from django.http import HttpResponse
from APP.models import Autos, Licencias, Motos
from django.template import loader
from APP.forms import AutosBusquedaFormulario, FormularioLicencias
# Create your views here.

def lista_autos(request):
    context = {}
    context["autos"] = Autos.objects.all()
    return render(request, "APP/lista_autos.html", context)

def crear_autos(request):
        if request.GET:
            marca= str(request.GET["marca"])
            modelo = int(request.GET["modelo"])
            objeto = Autos(marca=marca, modelo=modelo)
            objeto.save()
        info = Autos.objects.all()
        contexto = {"autos" : info}
        plantilla = loader.get_template("APP/crear-autos.html")
        documento = plantilla.render(contexto)
        return HttpResponse(documento)

def lista_motos(request):
    context = {}
    context["motos"] = Motos.objects.all()
    return render(request, "APP/lista_motos.html", context)

def crear_motos(request):
        if request.GET:
            marca= str(request.GET["marca"])
            modelo = int(request.GET["modelo"])
            objeto = Motos(marca=marca, modelo=modelo)
            objeto.save()
        info = Motos.objects.all()
        contexto = {"motos" : info}
        plantilla = loader.get_template("APP/crear-motos.html")
        documento = plantilla.render(contexto)
        return HttpResponse(documento)

def formulariolicencias(request):
    if request.method == 'POST':
        miFormulario = FormularioLicencias(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            licencias = Licencias(nombre = informacion['nombre'], apellido = informacion['apellido'], edad = informacion['edad'], email = informacion['email'])
            licencias.save()
            return render(request, "APP/verificacion.html")
    else:
        miFormulario= FormularioLicencias()
    return render(request, "APP/licencias.html",{"miFormulario":miFormulario})

def lista_registros(request):
    context = {}
    context["Licencias"] = Licencias.objects.all()
    return render(request, "APP/lista_licencias.html", context)

def buscar(request):
    if request.GET:
        var = request.GET["buscar"]

        buscadorC = Autos.objects.filter(marca__icontains = var)
        buscadorM = Motos.objects.filter(marca__icontains = var)

        if request.GET["palanca"] == "autos":
            contexto = { "buscados" : buscadorC }
        elif request.GET["palanca"] == "motos":
            contexto = { "buscados" : buscadorM }

        plantilla = loader.get_template("APP/buscador.html")
        documento = plantilla.render( contexto )
        return HttpResponse( documento )

    plantilla = loader.get_template("APP/buscador.html")
    documento = plantilla.render()
    return HttpResponse( documento )