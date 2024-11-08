from django.db import models

# Create your models here.
class Confederacion(models.Model):
    nombre = models.CharField(max_length=100)
    continente = models.CharField(max_length=50) 

    def __str__(self):
        return self.nombre
class Seleccion(models.Model):
    nombre = models.CharField(max_length=100)
    confederacion = models.ForeignKey(Confederacion, on_delete=models.CASCADE, related_name='seleccion')
    
    def __str__(self):
        return self.nombre                                     

class Futbolista(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=100, default='')
    fecha_nac = models.DateField()
    #El apartado posiciones es codido generado por Chat-GPT
    POSICIONES = [
        ('POR', 'Portero'),
        ('DEF', 'Defensa'),
        ('MED', 'Mediocampista'),
        ('DEL', 'Delantero'),
    ]
    posicion = models.CharField(
        max_length=3,         # Cambiado a 3 porque usamos abreviaturas de 3 letras
        choices=POSICIONES,   # Opciones predefinidas
        default='MED',        # Valor por defecto: Mediocampista
    )

    seleccion = models.ForeignKey(Seleccion, on_delete=models.CASCADE, related_name='futbolista')
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    