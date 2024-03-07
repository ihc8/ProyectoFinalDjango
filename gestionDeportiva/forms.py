from django import forms
from gestionDeportiva.widget import DatePickerInput, DateTimePickerInput, TimePickerInput
from .models import Deporte,Instalacion,Equipo,Jugador,Partido
from django.core.validators import MinValueValidator

class DeporteForm(forms.ModelForm):
    class Meta:
        model = Deporte
        fields = ['nombre']

class InstalacionForm(forms.ModelForm):
    class Meta:
        model = Instalacion
        fields = ["nombre", "direccion", "iluminacion", "cubierta"]
        widgets = {
           
            "nombre": forms.TextInput(attrs={"class":"form-control"}),
            "direccion": forms.TextInput(attrs={"class":"form-control"}),
            "iluminacion": forms.CheckboxInput(attrs={"class":"form-check-input"}),
            "cubierta": forms.CheckboxInput(attrs={"class":"form-check-input"}),
        }

class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = ["nombre", "id_deporte", "equipacion_principal", "equipacion_suplente", "contacto", "telefono", "email"]
        widgets = {
            "nombre": forms.TextInput(attrs={"class":"form-control"}),
            "id_deporte": forms.Select(attrs={"class":"form-control"}),
            "equipacion_principal": forms.TextInput(attrs={"class":"form-control"}),
            "equipacion_suplente": forms.TextInput(attrs={"class":"form-control"}),
            "contacto": forms.TextInput(attrs={"class":"form-control"}),
            "telefono": forms.TextInput(attrs={"class":"form-control"}),
            "email": forms.EmailInput(attrs={"class":"form-control"}),
            
         }

class JugadorForm(forms.ModelForm):
    class Meta:
        model = Jugador
        fields = ["nombre", "apellido1", "apellido2", "id_equipo", "dorsal","fecha_nacimiento" , "altura", "peso", "telefono"]
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "apellido1": forms.TextInput(attrs={"class": "form-control"}),
            "apellido2": forms.TextInput(attrs={"class": "form-control"}),
            "id_equipo": forms.Select(attrs={"class": "form-control"}, choices=[]),  
            "dorsal": forms.TextInput(attrs={"class": "form-control"}),
            "fecha_nacimiento" : DatePickerInput(),
          
            "altura": forms.TextInput(attrs={"class": "form-control"}),
            "peso": forms.TextInput(attrs={"class": "form-control"}),
            "telefono": forms.TextInput(attrs={"class": "form-control"}),
        }

    def __init__(self, *args, **kwargs):
        super(JugadorForm, self).__init__(*args, **kwargs)
        
        self.fields['id_equipo'].queryset = Equipo.objects.all()
        self.fields['id_equipo'].label_from_instance = lambda obj: "%s" % obj.nombre

class PartidoForm(forms.ModelForm):
    class Meta:
        model = Partido
        fields = ["id_deporte", "id_local", "puntos_local", "id_visitante", "puntos_visitante", "id_instalacion", "fecha_hora"]
        widgets = {
            "id_deporte": forms.Select(attrs={"class": "form-control"}),
            "id_local": forms.Select(attrs={"class": "form-control"}),
            "puntos_local": forms.NumberInput(attrs={"class": "form-control"}),
            "id_visitante": forms.Select(attrs={"class": "form-control"}),
            "puntos_visitante": forms.NumberInput(attrs={"class": "form-control"}),
            "id_instalacion": forms.Select(attrs={"class": "form-control"}),
            "fecha_hora": DateTimePickerInput(),
        }

    puntos_local = forms.IntegerField(validators=[MinValueValidator(0)])
    puntos_visitante = forms.IntegerField(validators=[MinValueValidator(0)])

    def clean(self):
        cleaned_data = super().clean()
        id_local = cleaned_data.get("id_local")
        id_visitante = cleaned_data.get("id_visitante")

        if id_local == id_visitante:
            raise forms.ValidationError("El equipo local y el visitante no pueden ser el mismo.")

        return cleaned_data
    def __init__(self, *args, **kwargs):
        super(PartidoForm, self).__init__(*args, **kwargs)
        # Limitar las opciones de id_local e id_visitante a solo los nombres de equipos
        self.fields['id_local'].queryset = Equipo.objects.all()
        self.fields['id_local'].label_from_instance = lambda obj: "%s" % obj.nombre
        self.fields['id_visitante'].queryset = Equipo.objects.all()
        self.fields['id_visitante'].label_from_instance = lambda obj: "%s" % obj.nombre
        self.fields['id_instalacion'].queryset = Instalacion.objects.all()
        self.fields['id_instalacion'].label_from_instance = lambda obj: "%s" % obj.nombre



