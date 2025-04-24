from django.db import models
# Create your models here.

class Partido(models.Model):
    fecha = models.DateField()
    rival = models.CharField(max_length=100)
    lugar = models.CharField(max_length=100)
    resultado = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.fecha} - {self.rival} ({self.lugar})" 

class Jugador(models.Model):
    nombre = models.CharField(max_length=100)
    posicion = models.CharField(max_length=50)
    numero = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} - {self.posicion} (#{self.numero})"