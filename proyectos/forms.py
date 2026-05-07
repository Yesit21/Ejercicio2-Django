from django import forms
from .models import Proyecto


class ProyectoForm(forms.ModelForm):

    class Meta:
        model = Proyecto
        fields = ['titulo', 'descripcion']


class ProyectoUpdateForm(forms.ModelForm):

    class Meta:
        model = Proyecto
        fields = ['titulo', 'descripcion']