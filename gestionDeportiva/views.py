import datetime
from django.views import generic
from django.shortcuts import redirect, render
from .import models
from django.views.generic import ListView
from .forms import DeporteForm,InstalacionForm,EquipoForm,JugadorForm,PartidoForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.db.models import Q

def inicio(request):
    fecha_actual = datetime.now().strftime("%d/%m/%Y")
    return render(request, 'base.html', {'fecha_actual': fecha_actual})

def home(request):
    template_name = 'home.html'
    context = get_context_data()

    return render(request, template_name, context)

def get_context_data():
    context = {}

    # Obtener todos los partidos
    partidos = models.Partido.objects.all()

    # Separar partidos jugados y por jugar
    fecha_actual = datetime.now()
    context['ultimos_partidos'] = partidos.filter(fecha_hora__lt=fecha_actual).order_by('-fecha_hora')[:5]
    context['proximos_partidos'] = partidos.filter(fecha_hora__gt=fecha_actual).order_by('fecha_hora')[:5]

    return context

    

class CustomLoginView(LoginView):
    template_name = 'login/login.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        if self.request.user.is_authenticated:
          
            return redirect('gestioDeportiva:home')
        return response




#DEPORTES



class listadoDeporteView(ListView):
    model = models.Deporte
    template_name = "deporte/listado_deportes.html"
    context_object_name = "deportes"
    paginate_by = 5 

    def get_queryset(self):
        query = self.request.GET.get("search")
        if query:
           
            return models.Deporte.objects.filter(Q(nombre__icontains=query)).order_by("nombre")
        else:
           
            return models.Deporte.objects.all().order_by("nombre")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        deportes = context["deportes"]

        paginator = Paginator(deportes, self.paginate_by)
        page = self.request.GET.get("page")

        try:
            deportes = paginator.page(page)
        except PageNotAnInteger:
            
            deportes = paginator.page(1)
        except EmptyPage:
            
            deportes = paginator.page(paginator.num_pages)

        context["deportes"] = deportes
        context["paginator"] = paginator  
        return context


class DeporteCreateView(generic.CreateView):
    model = models.Deporte
    template_name = 'deporte/creacion_deporte.html'
    form_class = DeporteForm
    success_url = '/gestionDeportiva/listado_deportes/' 
    
    

    

class DeporteUpdateView(generic.UpdateView):
    model = models.Deporte
    template_name = 'deporte/creacion_deporte.html'
    form_class = DeporteForm
    success_url = '/gestionDeportiva/listado_deportes/'

class DeporteDeleteView(generic.DeleteView):
    model = models.Deporte
    template_name = 'deporte/eliminar_deporte.html'
    success_url = '/gestionDeportiva/listado_deportes/'

#INSTALACIONES

class listadoInstalacionesView(generic.ListView):
    model = models.Instalacion
    template_name = "instalacion/listado_instalaciones.html"
    context_object_name = "instalaciones"
    paginate_by = 5  

    def get_queryset(self):
        return models.Instalacion.objects.all().order_by('nombre')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        instalaciones = context['instalaciones']

        paginator = Paginator(instalaciones, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            instalaciones = paginator.page(page)
        except PageNotAnInteger:
            
            instalaciones = paginator.page(1)
        except EmptyPage:
            
            instalaciones = paginator.page(paginator.num_pages)

        context['instalaciones'] = instalaciones
        context['paginator'] = paginator  
        return context
class InstalacionCreateView(generic.CreateView):
    model = models.Instalacion
    template_name = 'instalacion/crear_instalacion.html'
    form_class = InstalacionForm
    success_url = '/gestionDeportiva/listado_instalaciones/'

class InstalacionUpdateView(generic.UpdateView):
    model = models.Instalacion
    template_name = 'instalacion/crear_instalacion.html'
    form_class = InstalacionForm
    success_url = '/gestionDeportiva/listado_instalaciones/'

class InstalacionDeleteView(generic.DeleteView):
    model = models.Instalacion
    template_name = 'instalacion/eliminar_instalacion.html'
    success_url = '/gestionDeportiva/listado_instalaciones/'

#EQUIPOS
class listadoEquiposView(generic.ListView):
    model = models.Equipo
    template_name = "equipo/listado_equipos.html"
    context_object_name = "equipos"
    paginate_by = 5 

    def get_queryset(self):
        return models.Equipo.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        equipos = context['equipos']

        paginator = Paginator(equipos, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            equipos = paginator.page(page)
        except PageNotAnInteger:
            
            equipos = paginator.page(1)
        except EmptyPage:
           
            equipos = paginator.page(paginator.num_pages)

        context['equipos'] = equipos
        context['paginator'] = paginator 
        return context
class EquipoCreateView(generic.CreateView):
    model = models.Instalacion
    template_name = 'equipo/crear_equipo.html'
    form_class = EquipoForm
    success_url = '/gestionDeportiva/listado_equipos/'

class EquipoUpdateView(generic.UpdateView):
    model = models.Equipo
    template_name = 'equipo/crear_equipo.html'
    form_class = EquipoForm
    success_url = '/gestionDeportiva/listado_equipos/'

class EquipoDeleteView(generic.DeleteView):
    model = models.Equipo
    template_name = 'equipo/eliminar_equipo.html'
    success_url = '/gestionDeportiva/listado_equipos/'

class EquipoDetailView(generic.DetailView):
    model = models.Equipo
    template_name = 'equipo/equipo_informacion.html'
    context_object_name = 'equipo'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        equipo = self.object
        jugadores = models.Jugador.objects.filter(id_equipo=equipo.id_equipo).order_by('dorsal')
        context["jugadores"] = jugadores
        return context 

#JUGADORES
class listadoJugadoresView(generic.ListView):
    model = models.Jugador
    template_name = "jugador/listado_jugadores.html"
    context_object_name = "jugadores"
    paginate_by = 5 

    def get_queryset(self):
        return models.Jugador.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        jugadores = context['jugadores']

        paginator = Paginator(jugadores, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            jugadores = paginator.page(page)
        except PageNotAnInteger:
            
            jugadores = paginator.page(1)
        except EmptyPage:
            
            jugadores = paginator.page(paginator.num_pages)

        context['jugadores'] = jugadores
        context['paginator'] = paginator  
        return context

class JugadorCreateView(generic.CreateView):
    model = models.Jugador
    template_name = 'jugador/crear_jugador.html'
    form_class = JugadorForm
    success_url = '/gestionDeportiva/listado_jugadores/'

class JugadorUpdateView(generic.UpdateView):
    model = models.Jugador
    template_name = 'jugador/crear_jugador.html'
    form_class = JugadorForm
    success_url = '/gestionDeportiva/listado_jugadores/'

class JugadorDeleteView(generic.DeleteView):
    model = models.Jugador
    template_name = 'jugador/eliminar_jugador.html'
    success_url = '/gestionDeportiva/listado_jugadores/'

class JugadorDetailView(generic.DetailView):
    model = models.Jugador
    template_name = 'jugador/jugador_informacion.html'
    context_object_name = 'jugador'

#PARTIDOS
class listadoPartidosView(generic.ListView):
    model = models.Partido
    template_name = "partido/listado_partidos.html"
    context_object_name = "partidos"
    paginate_by = 5 
    ordering = ['-fecha_hora']

    def get_queryset(self):
        return models.Partido.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        partidos = context['partidos']

        paginator = Paginator(partidos, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            partidos = paginator.page(page)
        except PageNotAnInteger:
           
            partidos = paginator.page(1)
        except EmptyPage:
            # Si la página está fuera de rango, mostrar la última página
            partidos = paginator.page(paginator.num_pages)

        context['partidos'] = partidos
        context['paginator'] = paginator  
        return context

class PartidoCreateView(generic.CreateView):
    model = models.Partido
    template_name = 'partido/crear_partido.html'
    form_class = PartidoForm
    success_url = '/gestionDeportiva/listado_partidos/'

  

class PartidoUpdateView(generic.UpdateView):
    model = models.Partido
    template_name = 'partido/crear_partido.html'
    form_class = PartidoForm
    success_url = '/gestionDeportiva/listado_partidos/'

class PartidoDeleteView(generic.DeleteView):
    model = models.Partido
    template_name = 'partido/eliminar_partido.html'
    success_url = '/gestionDeportiva/listado_partidos/'

class PartidoDetailView(generic.DetailView):
    model = models.Partido
    template_name = 'partido/partido_informacion.html'
    context_object_name = 'partido'
