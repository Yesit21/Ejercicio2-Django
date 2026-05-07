from django.db import models
from django.contrib.auth.models import User
from proyectos.models import Proyecto

class Comentario(models.Model):
    proyecto = models.ForeignKey(Proyecto, related_name='comentarios', on_delete=models.CASCADE, verbose_name='Proyecto')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuario')
    texto = models.TextField(verbose_name='Comentario')
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')

    class Meta:
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'
        ordering = ['fecha_creacion']

    def __str__(self):
        return f"Comentario de {self.usuario.username} en {self.proyecto.titulo}"
