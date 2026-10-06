from django import forms
from .models import Cita


class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ['nombre_cliente', 'telefono', 'servicio', 'fecha', 'hora', 'estado']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'hora': forms.TimeInput(attrs={'type': 'time'}),
        }
