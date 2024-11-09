from django.contrib import admin
from django.urls import path, include 
from . import views

urlpatterns = [
    path('inicio',views.index,name='index'),

    #Listado de confederaciones
    path('listaConfederaciones/', views.listaConfederacion,name='listaConfederacion'),
    #Detalle de confederaciones
    path('detalleConfederacion/<int:id_confederacion>/', views.detalleConfederacion,name='detalleConfederacion'),
    #Listado de selecciones
    path('listaSelecciones/', views.listaSeleccion,name='listaSeleccion'),
    #Detalle de seleccion
    path('detalleSeleccion/<int:id_seleccion>/', views.detalleSeleccion,name='detalleSeleccion'),
    #Listado de futbolistas
    path('listaFutbolistas/', views.listaFutbolista,name='listaFutbolista'),
    #Detalle de futbolista
    path('detalleFutbolista/<int:id_futbolista>/', views.detalleFutbolista,name='detalleFutbolista'),
]