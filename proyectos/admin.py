from django.contrib import admin
from .models import Proyecto

@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'estudiante', 'estado', 'fecha_envio', 'calificacion')
    list_filter = ('estado', 'fecha_envio')
    search_fields = ('titulo', 'estudiante__username')
    readonly_fields = ('fecha_envio',)
    
    fieldsets = (
        ('Información del Proyecto', {
            'fields': ('titulo', 'descripcion', 'estudiante', 'documento')
        }),
        ('Estado y Evaluación', {
            'fields': ('estado', 'calificacion', 'fecha_revision')
        }),
        ('Fechas', {
            'fields': ('fecha_envio',)
        }),
    )
