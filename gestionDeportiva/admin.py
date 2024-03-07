# admin.py

from django.contrib import admin
from .models import Deporte, Instalacion, Equipo, Jugador, Partido

# Registra los modelos en el panel de administración


# Define las clases ModelAdmin personalizadas para cada modelo
class DeporteAdmin(admin.ModelAdmin):
    list_display = ["id_deporte", "nombre"]
    search_fields = ["nombre"]
    list_filter = ["nombre"]

class InstalacionAdmin(admin.ModelAdmin):
    list_display = ["id_instalacion", "nombre", "direccion", "iluminacion", "cubierta"]
    search_fields = ["nombre", "direccion"]
    list_filter = ["nombre", "iluminacion", "cubierta"]

class EquipoAdmin(admin.ModelAdmin):
    list_display = ["id_equipo", "nombre", "id_deporte", "equipacion_principal", "equipacion_suplente", "contacto", "telefono", "email"]
    search_fields = ["nombre", "contacto"]
    list_filter = ["id_deporte"]

class JugadorAdmin(admin.ModelAdmin):
    list_display = ["id_jugador", "nombre", "apellido1", "apellido2", "id_equipo", "dorsal", "fecha_nacimiento", "altura", "peso", "telefono"]
    search_fields = ["nombre", "apellido1", "apellido2"]
    list_filter = ["id_equipo"]

class PartidoAdmin(admin.ModelAdmin):
    list_display = ["id_partido", "id_local", "id_visitante", "fecha_hora", "id_instalacion", "puntos_local", "puntos_visitante"]
    search_fields = ["id_local", "id_visitante"]
    list_filter = ["id_instalacion"]

admin.site.register(Deporte, DeporteAdmin)
admin.site.register(Instalacion, InstalacionAdmin)
admin.site.register(Equipo, EquipoAdmin)
admin.site.register(Jugador, JugadorAdmin)
admin.site.register(Partido, PartidoAdmin)