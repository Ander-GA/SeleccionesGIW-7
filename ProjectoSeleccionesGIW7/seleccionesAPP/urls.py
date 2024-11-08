from django.contrib import admin
from django.urls import path, include 
from . import views

urlpatterns = [
    path('inicio',views.index,name='index'),

    #Listado de confederaciones
    path('listadoDeConfederaciones', views.listaConfederacionConPlantillas,name='listaC'),
    #Detalle de confederaciones
    path('listadoDeConfederaciones/<int:id_confederacion', views.detalleConfederacionConPlantillas,name='detalleC'),
    #Listado de selecciones
    path('listadoDeSelecciones', views.listaSeleccionPlantillas,name='listaS'),
    #Detalle de seleccion
    path('listadoDeSelecciones/<int:id_seleccion', views.detalleSeleccionPlantillas,name='detalleS'),
    #Listado de futbolistas
    path('listadoDeFutbolistas', views.listaFutbolistaConPlantillas,name='listaF'),
    #Detalle de futbolista
    path('listadoDeFutbolistas/<int:id_futbolista', views.detalleFutbolistaConPlantillas,name='detalleF'),
]