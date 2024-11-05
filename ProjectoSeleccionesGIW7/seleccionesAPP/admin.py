from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Confederacion, Seleccion, Futbolista

admin.site.register(Confederacion)
admin.site.register(Seleccion)
admin.site.register(Futbolista)