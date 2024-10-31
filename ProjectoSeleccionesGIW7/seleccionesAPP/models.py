from django.db import models

# Create your models here.
class Confederacion(models.Model):
    nombre = models.CharField(max_length=100)
    continente = models.CharField(max_length=50) 
    
    def __str__(self):
        return self.name

class Seleccion(models.Model):
    nombre = models.CharField(max_length=100)
    confederacion = models.ForeignKey(Confederacion, on_delete=models.CASCADE, related_name='seleccion')
                                      
    def __str__(self):
        return self.name

class Futbolista(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    posicion = models.CharField(max_length=50)  # Ej: Portero, Defensa, Mediocampista, Delantero
    seleccion = models.ForeignKey(Seleccion, on_delete=models.CASCADE, related_name='futbolista')
    def __str__(self):
        return self.name