# filepath: c:\Users\ext84003\Python\Django\blog\urls.py
from django.urls import path
from blog.views import equipo, listar_partidos, agregar_jugador, buscar_jugadores, home, jugadorList, jugadorDetail, jugadorCreate, jugadorUpdate, jugadorDelete

app_name = "blog"

urlpatterns = [
    path("equipo", equipo, name="equipo"),
    path("partidos", listar_partidos, name="partidos"),
    path("agregar-jugador", agregar_jugador, name="agregar_jugador"),
    path("buscar-jugadores", buscar_jugadores, name="buscar_jugadores"),
    path("home", home, name="home"),
    path('', home, name='root'),
    # CBV
    path("cbv/alta-jugador",jugadorCreate.as_view(), name="cbv-alta-jugador"),
    path("cbv/jugadores-list", jugadorList.as_view(), name="cbv-lista-jugadores"),
    path("cbv/jugador/<int:pk>/", jugadorDetail.as_view(), name="cbv-jugador-detail"),
    path("cbv/jugador/<int:pk>/editar", jugadorUpdate.as_view(), name="cbv-jugador-editar"),
    path("cbv/jugador/<int:pk>/eliminar", jugadorDelete.as_view(), name="cbv-jugador-eliminar"),
]