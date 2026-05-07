from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Proyecto(models.Model):

    ESTADOS = [
        ('enviado', 'Enviado'),
        ('revision', 'Revisión'),
        ('aprobado', 'Aprobado'),
    ]

    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()

    estudiante = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    estado = models.CharField(
        max_length=20,
        choices=ESTADOS,
        default='enviado'
    )

    calificacion = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True
    )

    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse(
            'proyecto_detail',
            kwargs={'pk': self.pk}
        )