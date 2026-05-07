from django import forms

from .models import Comentario


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ("texto",)
        labels = {
            "texto": "Comentario",
        }
        widgets = {
            "texto": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Escribe tu comentario aquí...",
                    "rows": 4,
                }
            ),
        }
