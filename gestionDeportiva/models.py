
from django.db import models
from django.core.validators import MinValueValidator




class Deporte(models.Model):
    id_deporte = models.IntegerField(primary_key = True)
    nombre = models.CharField(max_length = 50)        
        
    class Meta:        
        verbose_name_plural = "Deportes"
        db_table = "deportes"        
    def __str__(self):
        return f"{self.id_deporte} {self.nombre}"


class Instalacion(models.Model):
    id_instalacion = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length = 50)      
    direccion = models.CharField(max_length=100)
    iluminacion = models.BooleanField(default=False)
    cubierta = models.BooleanField(default=False)
    class Meta:        
        verbose_name_plural = "Instalaciones"
        db_table = "instalaciones"
    def __str__(self):
        return f"{self.id_instalacion} {self.nombre} {self.nombre} {self.direccion} {self.iluminacion} {self.cubierta}"
    
class Equipo(models.Model):
    id_equipo = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50, unique=True)
    id_deporte = models.ForeignKey('Deporte', on_delete=models.RESTRICT, db_column='id_deporte')
    equipacion_principal = models.CharField(max_length=100)
    equipacion_suplente = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    email = models.EmailField() 
    class Meta:
        verbose_name_plural = "Equipos"
        db_table = "equipos"
    def __str__(self):
        return f"{self.id_equipo} {self.nombre} {self.id_deporte} {self.equipacion_principal} {self.equipacion_suplente} {self.contacto} {self.telefono} {self.email}"
    

    
class Jugador(models.Model):
    id_jugador = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido1 = models.CharField(max_length=50)
    apellido2 = models.CharField(max_length=50, blank=True, null=True)
    id_equipo = models.ForeignKey('Equipo', on_delete=models.RESTRICT, db_column='id_equipo')
    dorsal = models.IntegerField()
    fecha_nacimiento = models.DateField()
    altura = models.DecimalField(max_digits=3, decimal_places=2)
    peso = models.PositiveIntegerField()
    telefono = models.CharField(max_length=15)

    class Meta:
        verbose_name_plural = "Jugadores"
        db_table = "jugadores"
        unique_together = ['id_equipo', 'dorsal']  
    def __str__(self):
        return f"{self.id_jugador} {self.nombre} {self.apellido1} {self.apellido2} {self.id_equipo.id_equipo} {self.dorsal} {self.fecha_nacimiento} {self.altura} {self.peso} {self.telefono}"
    
class Partido(models.Model):
    id_partido = models.IntegerField(primary_key=True)
    id_deporte = models.ForeignKey('Deporte', on_delete=models.RESTRICT, db_column='id_deporte')
    fecha_hora = models.DateTimeField()
    id_instalacion = models.ForeignKey('Instalacion', on_delete=models.RESTRICT, blank=True, null=True, db_column='id_instalacion')
    id_local = models.ForeignKey('Equipo', related_name='partidos_local', on_delete=models.RESTRICT, db_column='id_local')
    id_visitante = models.ForeignKey('Equipo', related_name='partidos_visitante', on_delete=models.RESTRICT, db_column='id_visitante')
    puntos_local = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    puntos_visitante = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    observaciones = models.CharField(max_length=200, blank=True)

    class Meta:
        verbose_name_plural = "Partidos"
        db_table = "partidos"

    def __str__(self):
        return f"{self.id_partido} {self.id_deporte} {self.fecha_hora} {self.id_instalacion} {self.id_local} vs {self.id_visitante} - {self.puntos_local} {self.puntos_visitante} {self.observaciones}"