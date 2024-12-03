from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from .models import Confederacion, Seleccion, Futbolista

from django.views.generic import ListView,DetailView

# Vistas de lista
def index(request):
    return render(request, 'index.html')

#SELECCIONES 
#def listaSeleccion(request):
#    seleccion = Seleccion.objects.order_by('nombre')
#    contexto = {'seleccion_list': seleccion}
#    return render(request, 'listaSeleccion.html', contexto)
#
#def detalleSeleccion(request, id_seleccion):
#    seleccion = get_object_or_404(Seleccion, pk=id_seleccion)
#    contexto = {'seleccion': seleccion}
#    return render(request, 'detalleSeleccion.html', contexto)
#
#JUGADORES
#def listaFutbolista(request):
#    futbolistas = Futbolista.objects.order_by('nombre')
#    contexto = {'futbolista_list' : futbolistas}
#    return render(request, 'listaFutbolista.html', contexto)
#
#def detalleFutbolista(request, id_futbolista):
#    futbolista = get_object_or_404(Futbolista, pk=id_futbolista)
#    contexto = {'futbolista': futbolista}
#    return render(request, 'detalleFutbolista.html', contexto)
#
#CONFEDERACION
#def listaConfederacion(request):
#    confederacion = Confederacion.objects.order_by('nombre')
#    contexto = {'confederacion_list' : confederacion}
#    return render(request, 'listaConfederacion.html', contexto)
#
#def detalleConfederacion(request, id_confederacion):
#    confederacion = get_object_or_404(Confederacion, pk=id_confederacion)
#    contexto = {'confederacion': confederacion}
#    return render(request, 'detalleConfederacion.html', contexto)
#
#

#VISTAS CONFEDERACION (0,75)
class detalleConfederacion(DetailView):
    model=Confederacion
    template_name='detalleConfederacion.html'
    context_object_name='confederacion'

class listaConfederacion(ListView):
    model= Confederacion
    template_name='listaConfederacion.html'
    context_object_name='confederacion_list'

#VISTAS SELECCION
class detalleSeleccion(DetailView):
    model=Seleccion
    template_name='detalleSeleccion.html'
    context_object_name='seleccion'

class listaSeleccion(ListView):
    model= Seleccion
    template_name='listaSeleccion.html'
    context_object_name='seleccion_list'

#VISTAS JUGADORES
class detalleFutbolista(DetailView):
    model=Futbolista
    template_name='detalleFutbolista.html'
    context_object_name='futbolista'

class listaFutbolista(ListView):
    model= Futbolista
    template_name='listaFutbolista.html'
    context_object_name='futbolista_list'
    queryset=Futbolista.objects.order_by('nombre')