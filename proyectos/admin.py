from django.contrib import admin
from .models import Proyecto


@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):

    list_display = (
        'titulo',
        'estudiante',
        'estado',
        'calificacion',
        'creado'
    )

    list_filter = (
        'estado',
        'creado'
    )

    search_fields = (
        'titulo',
        'estudiante__username'
    )

    fieldsets = (

        ('Información del Proyecto', {
            'fields': (
                'titulo',
                'descripcion',
                'estudiante'
            )
        }),

        ('Estado y Evaluación', {
            'fields': (
                'estado',
                'calificacion'
            )
        }),

    )