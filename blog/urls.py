from django.urls import path

from blog.views import equipo, listar_partidos

urlpatterns = [
    path("equipo", equipo, name="equipo"),
    path("partidos", listar_partidos, name="partidos")
]