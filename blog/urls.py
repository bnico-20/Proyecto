# filepath: c:\Users\ext84003\Python\Django\blog\urls.py
from django.urls import path
from blog.views import equipo, listar_partidos, agregar_jugador, buscar_jugadores

app_name = "blog"

urlpatterns = [
    path("equipo", equipo, name="equipo"),
    path("partidos", listar_partidos, name="partidos"),
    path("agregar-jugador", agregar_jugador, name="agregar_jugador"),
    path("buscar-jugadores", buscar_jugadores, name="buscar_jugadores"),
]