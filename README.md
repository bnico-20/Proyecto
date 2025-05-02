Bertin FC
Bertin FC es una aplicación web desarrollada en Django para gestionar un equipo de fútbol. Permite realizar operaciones como agregar, editar, eliminar y buscar jugadores, así como listar partidos y mostrar información sobre el equipo.

--Características principales

1-Gestión de jugadores:

Agregar nuevos jugadores al equipo.
Editar la información de los jugadores existentes.
Eliminar jugadores del equipo.
Buscar jugadores por nombre, posición o número.
Ver detalles de cada jugador, incluyendo su imagen.

2-Gestión de partidos:

Listar todos los partidos del equipo, mostrando información como fecha, rival, lugar y resultado.

3-Páginas informativas:

Página de inicio con un mensaje de bienvenida.
Página "About" con información sobre el equipo Bertin FC.

4-Autenticación de usuarios:

Inicio de sesión y registro de usuarios.
Edición del perfil del usuario, incluyendo la posibilidad de subir un avatar.
Cierre de sesión.

5-Diseño responsivo:

Todas las páginas están diseñadas con Bootstrap para un diseño moderno y responsivo.

-- Estructura del proyecto:

--Modelos:

-Jugador:

nombre: Nombre del jugador.
posicion: Posición en el campo.
numero: Número de camiseta.
imagen: Imagen del jugador (opcional).

-Partido:

fecha: Fecha del partido.
rival: Nombre del equipo rival.
lugar: Lugar donde se jugó el partido.
resultado: Resultado del partido.


--Vistas

-Vistas basadas en funciones (FBV):
1- equipo:

Muestra la lista de jugadores del equipo.
URL: /blog/equipo/

2-listar_partidos:

Muestra la lista de partidos.
URL: /blog/partidos/

3-agregar_jugador:

Permite agregar un nuevo jugador al equipo.
URL: /blog/agregar-jugador/

4-buscar_jugadores:

Permite buscar jugadores por nombre, posición o número.
URL: /blog/buscar-jugadores/

5-about:

Muestra información sobre el equipo Bertin FC.
URL: /blog/about/

-Vistas basadas en clases (CBV):

1-jugadorList:

Lista todos los jugadores.
URL: /blog/cbv/jugadores-list/

2-jugadorListFiltered:

Lista jugadores con filtros avanzados (nombre, posición, número).
URL: /blog/cbv/jugador-list-filtered/

3-jugadorDetail:

Muestra los detalles de un jugador.
URL: /blog/cbv/jugador/<int:pk>/

4-jugadorCreate:

Permite agregar un nuevo jugador.
URL: /blog/cbv/alta-jugador/

5-jugadorUpdate:

Permite editar la información de un jugador.
URL: /blog/cbv/jugador/<int:pk>/editar/

6-jugadorDelete:

Permite eliminar un jugador.
URL: /blog/cbv/jugador/<int:pk>/eliminar/

--Templates

1- base.html:

Plantilla base que incluye la barra de navegación y el diseño general del sitio.

2- equipo.html:

Muestra la lista de jugadores del equipo.

3- partidos.html:

Muestra la lista de partidos.

4- jugador-create.html:

Formulario para agregar un nuevo jugador.

5- jugador-update.html:

Formulario para editar un jugador existente.

6- jugador-detail.html:

Muestra los detalles de un jugador, incluyendo su imagen.

7- buscar-jugadores.html:

Página con un formulario de búsqueda y resultados de jugadores.

8- about.html:

Página informativa sobre el equipo Bertin FC.

-- Diseño
El diseño del sitio utiliza Bootstrap para garantizar un diseño moderno y responsivo. Algunas características clave incluyen:

-Barra de navegación: Acceso rápido a las principales secciones del sitio.
-Tarjetas: Los jugadores y partidos se muestran en tarjetas organizadas en cuadrículas.
-Formularios estilizados: Los formularios para agregar y editar jugadores están centrados y estilizados con Bootstrap.

--Autenticación

-Inicio de sesión: Los usuarios pueden iniciar sesión para acceder a las funcionalidades protegidas.
-Registro: Los nuevos usuarios pueden registrarse en el sitio.
-Edición de perfil: Los usuarios pueden editar su perfil y subir un avatar.
-Cierre de sesión: Los usuarios pueden cerrar sesión desde la barra de navegación.

link video: https://drive.google.com/drive/u/0/folders/1EwRjTBf7EeEj57Mb7yI8Io0-2KF7yw6L