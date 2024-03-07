from django.urls import path
from . import views

app_name = "gestioDeportiva"
urlpatterns = [
     #RUTAS GENERALES
      path('', views.CustomLoginView.as_view(), name="login"),
    
      path('inicio/', views.inicio, name="inicio"),
    
      path('home/', views.home, name="home"),
     #RUTAS DEPORTE
      path('listado_deportes/', views.listadoDeporteView.as_view(), name="listado_deportes"),
      path('crear_deporte/', views.DeporteCreateView.as_view(), name="crear_deporte"),
      path('editar_deporte/<int:pk>/', views.DeporteUpdateView.as_view(), name="editar_deporte"),
      path('eliminar_deporte/<int:pk>/', views.DeporteDeleteView.as_view(), name="eliminar_deporte"),

      #RUTAS INSTALACION
      path('listado_instalaciones/', views.listadoInstalacionesView.as_view(), name="listado_instalaciones"),
      path('crear_instalacion/', views.InstalacionCreateView.as_view(), name="crear_instalacion"),
      path('editar_instalacion/<int:pk>/', views.InstalacionUpdateView.as_view(), name="editar_instalacion"),
      path('eliminar_instalacion/<int:pk>/', views.InstalacionDeleteView.as_view(), name="eliminar_instalacion"),

      #RUTAS EQUIPO
      path('listado_equipos/', views.listadoEquiposView.as_view(), name="listado_equipos"),
      path('crear_equipo/', views.EquipoCreateView.as_view(), name="crear_equipo"),
      path('editar_equipo/<int:pk>/', views.EquipoUpdateView.as_view(), name="editar_equipo"),
      path('eliminar_equipo/<int:pk>/', views.EquipoDeleteView.as_view(), name="eliminar_equipo"),
      path('equipo_informacion/<int:pk>/', views.EquipoDetailView.as_view(), name="equipo_informacion"),

      #RUTAS JUGADOR
      path('listado_jugadores/', views.listadoJugadoresView.as_view(), name="listado_jugadores"),
      path('crear_jugador/', views.JugadorCreateView.as_view(), name="crear_jugador"),
      path('editar_jugador/<int:pk>/', views.JugadorUpdateView.as_view(), name="editar_jugador"),
      path('eliminar_jugador/<int:pk>/', views.JugadorDeleteView.as_view(), name="eliminar_jugador"),
      path('jugador_informacion/<int:pk>/', views.JugadorDetailView.as_view(), name="jugador_informacion"),

      #RUTAS PARTIDO
      path('listado_partidos/', views.listadoPartidosView.as_view(), name="listado_partidos"),
      path('crear_partido/', views.PartidoCreateView.as_view(), name="crear_partido"),
      path('editar_partido/<int:pk>/', views.PartidoUpdateView.as_view(), name="editar_partido"),
      path('eliminar_partido/<int:pk>/', views.PartidoDeleteView.as_view(), name="eliminar_partido"),
      path('partido_informacion/<int:pk>/', views.PartidoDetailView.as_view(), name="partido_informacion"),


]