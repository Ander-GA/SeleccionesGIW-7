from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Confederacion, Seleccion, Futbolista

#admin.site.register(Confederacion)
#admin.site.register(Seleccion)
#admin.site.register(Futbolista)

#MODIFICACION DE ADMIN 0.5
class ConfederacionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields':['nombre']}),
        ('Continente',{'fields':['continente']})
    ]
    list_display=('nombre','continente')
admin.site.register(Confederacion,ConfederacionAdmin)

class SeleccionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields':['nombre']}),
        ('Confederacion',{'fields':['confederacion']})
    ]
    list_display=('nombre','confederacion')
admin.site.register(Seleccion,SeleccionAdmin)

class FutbolistaAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Datos personales',{'fields':['nombre','apellido','fecha_nac']}),
        ('Datos del jugador',{'fields':['posicion','seleccion']}),
        ('Imagen',{'fields':['imagenFutbolista']})
    ]
    list_display=('nombre','apellido','seleccion')
admin.site.register(Futbolista,FutbolistaAdmin)