from django.contrib import admin
from django.urls import path, include 
from . import views

urlpatterns = [
    path('inicio',views.index,name='index'),

    #LISTADO DE CONFEDERACIONES
    #path('listaConfederaciones/', views.listaConfederacion,name='listaConfederacion'),
    path('listaConfederaciones/',views.listaConfederacion.as_view(),name='listaConfederacion'),
    #DETALLE DE CONFEDERACIONES
    #path('detalleConfederacion/<int:id_confederacion>/', views.detalleConfederacion,name='detalleConfederacion'),
    path('detalleConfederacion/<int:pk>', views.detalleConfederacion.as_view(),name='detalleConfederacion'),
    #LISTADO DE SELECCIONES
    #path('listaSelecciones/', views.listaSeleccion,name='listaSeleccion'),
    path('listaSelecciones/', views.listaSeleccion.as_view(),name='listaSeleccion'),
    #DETALLE DE SELECCION
    #path('detalleSeleccion/<int:id_seleccion>/', views.detalleSeleccion,name='detalleSeleccion'),
    path('detalleSeleccion/<int:pk>/', views.detalleSeleccion.as_view(),name='detalleSeleccion'),
    #LISTADO DE FUTBOLISTAS
    #path('listaFutbolistas/', views.listaFutbolista,name='listaFutbolista'),
    path('listaFutbolistas/', views.listaFutbolista.as_view(),name='listaFutbolista'),
    #DETALLE DE FUTBOLISTAS
    #path('detalleFutbolista/<int:id_futbolista>/', views.detalleFutbolista,name='detalleFutbolista')
    path('detalleFutbolista/<int:pk>/', views.detalleFutbolista.as_view(),name='detalleFutbolista')
]