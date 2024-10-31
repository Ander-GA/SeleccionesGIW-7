from django.shortcuts import render

# Create your views here.
#Listas
class ConfederacionListView(ListView):
    model = Confederacion
    template_name = 'futbol/confederacion_list.html'
    context_object_name = 'confederaciones'

class SeleccionListView(ListView):
    model = Seleccion
    template_name = 'futbol/seleccion_list.html'
    context_object_name = 'selecciones'

class FutbolistaListView(ListView):
    model = Futbolista
    template_name = 'futbol/futbolista_list.html'
    context_object_name = 'futbolistas'
    # Detalles
class ConfederacionDetailView(DetailView):
    model = Confederacion
    template_name = 'futbol/confederacion_detail.html'
    context_object_name = 'confederacion'

class SeleccionDetailView(DetailView):
    model = Seleccion
    template_name = 'futbol/seleccion_detail.html'
    context_object_name = 'seleccion'

class FutbolistaDetailView(DetailView):
    model = Futbolista
    template_name = 'futbol/futbolista_detail.html'
    context_object_name = 'futbolista'