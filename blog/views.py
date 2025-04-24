from django.shortcuts import render
from .models import Partido

# Create your views here.

def equipo(request): # en django se llama "view"
    return render(request, 'blog/equipo.html')

from blog.forms import BlogPartido

def listar_partidos(request):
    partidos = Partido.objects.all()  # Obtener todos los partidos
    return render(request, 'blog/partidos.html', {'listar_partidos': partidos})




    