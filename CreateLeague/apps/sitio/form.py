from django import forms

from apps.equipo.models import Equipo
from apps.liga.models import Liga


class LigaForm(forms.ModelForm):
    class Meta:
        model = Liga
        fields = ('nombre',)
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre',
                'style': 'font-size: 1.0rem;'
            }),
        }


class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = ("nombre", "jugados", "ganados", "empatados", "perdidos", "goles_a_favor", "goles_en_contra")

        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre',
                'style': 'font-size: 1.0rem;'
            }),
            'jugados': forms.NumberInput(attrs={
                'class': 'form-control',
                'style': 'font-size: 1.0rem;'
            }),
            'ganados': forms.NumberInput(attrs={
                'class': 'form-control',
                'style': 'font-size: 1.0rem;'
            }),
            'empatados': forms.NumberInput(attrs={
                'class': 'form-control',
                'style': 'font-size: 1.0rem;'
            }),
            'perdidos': forms.NumberInput(attrs={
                'class': 'form-control',
                'style': 'font-size: 1.0rem;'
            }),
            'goles_a_favor': forms.NumberInput(attrs={
                'class': 'form-control',
                'style': 'font-size: 1.0rem;'
            }),
            'goles_en_contra': forms.NumberInput(attrs={
                'class': 'form-control',
                'style': 'font-size: 1.0rem;'
            }),
        }