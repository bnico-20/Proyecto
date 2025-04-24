from django.db import models
# Create your models here.

class Partido(models.Model):
    fecha = models.DateField()
    rival = models.CharField(max_length=100)
    lugar = models.CharField(max_length=100)
    resultado = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.fecha} - {self.rival} ({self.lugar})" 
