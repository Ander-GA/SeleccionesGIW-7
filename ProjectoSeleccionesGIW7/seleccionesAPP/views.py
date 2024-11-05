from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import Confederacion, Seleccion, Futbolista

# Vistas de lista
def confederacion_list(request):
    confederaciones = Confederacion.objects.all()
    return render(request, 'confederacion_list.html', {'confederaciones': confederaciones})

def seleccion_list(request):
    selecciones = Seleccion.objects.all()
    return render(request, 'seleccion_list.html', {'selecciones': selecciones})

def futbolista_list(request):
    futbolistas = Futbolista.objects.all()
    return render(request, 'futbolista_list.html', {'futbolistas': futbolistas})

# Vistas de detalle
def confederacion_detalle(request, id_confederacion):
    try:
        confederacion = Confederacion.objects.get(pk=id_confederacion)
        selecciones = confederacion.selecciones.all()
        
        # Crear la cadena de texto con los detalles de la confederación
        cadenaDeTexto = f"{confederacion.nombre} - CIF: {confederacion.cif}\n"
        # Listar selecciones
        if selecciones.exists():
            cadenaDeTexto += "Selecciones:\n"
            for seleccion in selecciones:
                cadenaDeTexto += f"- {seleccion.nombre}\n"
        else:
            cadenaDeTexto += "No hay selecciones asociadas a esta confederación."
            
        return HttpResponse(cadenaDeTexto)
    except Confederacion.DoesNotExist:
        return HttpResponseNotFound("Confederación no encontrada")

# Vista de detalle para Seleccion
def detalle_seleccion(request, id_seleccion):
    try:
        seleccion = Seleccion.objects.get(pk=id_seleccion)
        futbolistas = seleccion.futbolistas.all() 
        # Crear la cadena de texto con los detalles de la selección
        cadenaDeTexto = f"{seleccion.nombre} - CIF: {seleccion.cif}\n"
        # Listar futbolistas
        if futbolistas.exists():
            cadenaDeTexto += "Futbolistas:\n"
            for futbolista in futbolistas:
                cadenaDeTexto += f"- {futbolista.nombre}, Posición: {futbolista.posicion}\n"
        else:
            cadenaDeTexto += "No hay futbolistas asociados a esta selección."
        return HttpResponse(cadenaDeTexto)
    except Seleccion.DoesNotExist:
        return HttpResponseNotFound("Selección no encontrada")

def futbolista_detail(request, id_futbolisa):
    try:
        futbolista = Futbolista.objects.get(pk=id_futbolisa)
        #Crear la cadena de texto con los detalles de la selección
        cadenaDeTexto = f"{futbolista.nombre} - Código: {futbolista.codigo}\n"
        if futbolista.exist():
            cadenaDeTexto += f"- {futbolista.nombre}, Posición: {futbolista.posicion}\n"
        else:
            cadenaDeTexto += "No hay futbolistas asociado."
        return HttpResponse(cadenaDeTexto)
    except Seleccion.DoesNotExist:
        return HttpResponseNotFound("Futbolista no encontrado")