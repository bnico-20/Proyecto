from django.shortcuts import render, redirect
from .models import Partido, Jugador
from .forms import BlogPartido, BlogJugador
from django.urls import reverse_lazy

def equipo(request):
    jugadores = Jugador.objects.all()
    return render(request, 'blog/equipo.html', {'jugadores': jugadores})

def listar_partidos(request):
    partidos = Partido.objects.all()  # Obtiene todos los partidos
    return render(request, 'blog/partidos.html', {'partidos': partidos})

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

def home(request):
    return render(request, 'blog/home.html')

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

#30/4
from django.contrib.auth.mixins import LoginRequiredMixin

class jugadorList(ListView, LoginRequiredMixin):
    model = Jugador
    template_name = 'blog/cbv/jugadores-list.html'
    context_object_name = 'jugadores'

from django.views.generic import ListView
from django.db.models import Q
from .models import Jugador

class jugadorListFiltered(ListView, LoginRequiredMixin):
    model = Jugador
    template_name = 'blog/cbv/jugador-list-filtered.html'
    context_object_name = 'jugadores'

    def get_queryset(self):
        queryset = super().get_queryset()

        # Extraer parámetros de búsqueda
        nombre = self.request.GET.get('nombre', '')
        posicion = self.request.GET.get('posicion', '')
        numero = self.request.GET.get('numero', '')


        if nombre:
            queryset = queryset.filter(nombre__icontains=nombre)
        if posicion:
            queryset = queryset.filter(posicion__icontains=posicion)
        if numero:
            queryset = queryset.filter(numero__icontains=numero)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filtros'] = {
            'nombre': self.request.GET.get('nombre', ''),
            'posicion': self.request.GET.get('posicion',''),
            'numero': self.request.GET.get('numero',''),
        }
        return context


class jugadorDetail(DetailView, LoginRequiredMixin):
    model = Jugador
    template_name = 'blog/cbv/jugador-detail.html'
    context_object_name = 'jugador'
    

class jugadorCreate(CreateView, LoginRequiredMixin):
    model = Jugador
    template_name = 'blog/cbv/jugador-create.html'
    fields = ['nombre', 'posicion','numero', 'imagen']
    success_url = reverse_lazy('blog:cbv-lista-jugadores')

class jugadorUpdate(UpdateView, LoginRequiredMixin):
    model = Jugador
    template_name = 'blog/cbv/jugador-update.html'
    fields = ['nombre', 'posicion','numero', 'imagen']
    success_url = reverse_lazy('blog:cbv-lista-jugadores')  # Redirige a la lista de jugadores

class jugadorDelete(DeleteView, LoginRequiredMixin):
    model = Jugador
    template_name = 'blog/cbv/jugador-delete.html'
    context_object_name = 'jugador'
    success_url = reverse_lazy('blog:cbv-lista-jugadores')

def about(request):
    return render(request, "blog/about.html") 