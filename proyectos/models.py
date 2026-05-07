from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError

class Proyecto(models.Model):
    ESTADOS = [
        ('enviado', 'Enviado'),
        ('revision', 'Revisión'),
        ('aprobado', 'Aprobado'),
    ]
    
    titulo = models.CharField(max_length=200, verbose_name='Título')
    descripcion = models.TextField(verbose_name='Descripción')
    estudiante = models.ForeignKey(User, related_name='proyectos', on_delete=models.CASCADE, verbose_name='Estudiante')
    documento = models.FileField(upload_to='proyectos/', verbose_name='Documento')
    estado = models.CharField(max_length=20, choices=ESTADOS, default='enviado', verbose_name='Estado')
    fecha_envio = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Envío')
    fecha_revision = models.DateTimeField(null=True, blank=True, verbose_name='Fecha de Revisión')
    calificacion = models.DecimalField(
        max_digits=4, 
        decimal_places=2, 
        null=True, 
        blank=True, 
        verbose_name='Calificación',
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)]
    )
    
    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
        ordering = ['-fecha_envio']
        permissions = [
            ('puede_revisar_proyecto', 'Puede revisar proyectos'),
            ('puede_calificar_proyecto', 'Puede calificar proyectos'),
        ]
    
    def __str__(self):
        return f"{self.titulo} - {self.estudiante.username}"
    
    def get_absolute_url(self):
        return reverse('proyecto_detail', kwargs={'pk': self.pk})
    
    def puede_agregar_comentarios(self):
        """Verifica si se pueden agregar comentarios al proyecto"""
        return self.estado != 'aprobado'
    
    def clean(self):
        if self.calificacion is not None:
            if self.calificacion < 0 or self.calificacion > 5:
                raise ValidationError({'calificacion': 'La calificación debe estar entre 0.0 y 5.0'})
        
        if self.estado == 'aprobado' and not self.calificacion:
            raise ValidationError({'calificacion': 'Debe asignar una calificación antes de aprobar el proyecto'})
