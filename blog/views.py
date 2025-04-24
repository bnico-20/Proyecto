from django.shortcuts import render, redirect
from .models import Partido, Jugador
from .forms import BlogPartido, BlogJugador

def equipo(request):
    return render(request, 'blog/equipo.html')

def listar_partidos(request):
    partidos = Partido.objects.all()
    return render(request, 'blog/partidos.html', {'listar_partidos': partidos})

def agregar_jugador(request):
    if request.method == "POST":
        formulario = BlogJugador(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('blog:buscar_jugadores')
    else:
        formulario = BlogJugador()
    return render(request, 'blog/form_jugador.html', {'formulario': formulario})

def buscar_jugadores(request):
    query = request.GET.get('q')  # Obtiene el valor del campo de búsqueda
    if query:
        jugadores = Jugador.objects.filter(nombre__icontains=query)  # Filtra jugadores por nombre
    else:
        jugadores = Jugador.objects.all()  # Muestra todos los jugadores si no hay búsqueda
    return render(request, 'blog/jugadores.html', {'jugadores': jugadores, 'query': query})


    