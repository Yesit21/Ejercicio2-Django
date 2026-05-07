from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Proyecto(models.Model):
    ESTADOS = [
        ('enviado', 'Enviado'),
        ('revisión', 'En Revisión'),
        ('aprobado', 'Aprobado'),
    ]
    
    titulo = models.CharField(max_length=200, verbose_name='Título')
    descripcion = models.TextField(verbose_name='Descripción')
    estudiante = models.ForeignKey(User, related_name='proyectos', on_delete=models.CASCADE, verbose_name='Estudiante')
    documento = models.FileField(upload_to='proyectos/', verbose_name='Documento')
    estado = models.CharField(max_length=20, choices=ESTADOS, default='enviado', verbose_name='Estado')
    fecha_envio = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Envío')
    fecha_revision = models.DateTimeField(null=True, blank=True, verbose_name='Fecha de Revisión')
    calificacion = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True, verbose_name='Calificación')
    
    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
        ordering = ['-fecha_envio']
    
    def __str__(self):
        return f"{self.titulo} - {self.estudiante.username}"
    
    def puede_agregar_comentarios(self):
        """Verifica si se pueden agregar comentarios al proyecto"""
        return self.estado != 'aprobado'
