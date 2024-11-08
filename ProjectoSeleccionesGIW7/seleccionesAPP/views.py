from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from .models import Confederacion, Seleccion, Futbolista

# Vistas de lista
def index(request):
    return render(request, 'index.html')

#SELECCIONES 
def listaSeleccionPlantillas(request):
    seleccion = Seleccion.objects.order_by('nombre')
    contexto = {'seleccion_list': seleccion}
    return render(request, 'listaSeleccion.html', contexto)

def detalleSeleccionPlantillas(request, id_seleccion):
    seleccion = get_object_or_404(Seleccion, pk=id_seleccion)
    contexto = {'seleccion': seleccion}
    return render(request, 'detalleSeleccion.html', contexto)

#JUGADORES
def listaFutbolistaConPlantillas(request):
    futbolistas = Futbolista.objects.order_by('nombre')
    contexto = {'futbolista_list' : futbolistas}
    return render(request, 'listaFutbolista.html', contexto)

def detalleFutbolistaConPlantillas(request, id_futbolista):
    futbolista = get_object_or_404(Futbolista, pk=id_futbolista)
    contexto = {'futbolista': futbolista}
    return render(request, 'detalleFutbolista.html', contexto)

#CONFEDERACION
def listaConfederacionConPlantillas(request):
    ciudad = Confederacion.objects.order_by('nombre')
    contexto = {'ciudad_list' : ciudad}
    return render(request, 'listaConfederacion.html', contexto)

def detalleConfederacionConPlantillas(request, id_ciudad):
    confederacion = get_object_or_404(Confederacion, pk=id_ciudad)
    contexto = {'confederacion': confederacion}
    return render(request, 'detalleConfederacion.html', contexto)


