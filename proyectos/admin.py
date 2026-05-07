from django.contrib import admin
from django.utils import timezone
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

    list_display = ('titulo', 'estudiante', 'estado', 'fecha_envio', 'calificacion')
    list_filter = ('estado', 'fecha_envio')
    search_fields = ('titulo', 'estudiante__username')
    readonly_fields = ('fecha_envio',)
    actions = ['aprobar_proyectos', 'marcar_en_revision']
    
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
        ('Fechas', {
            'fields': ('fecha_envio',)
        }),

    
    def aprobar_proyectos(self, request, queryset):
        """Acción para aprobar múltiples proyectos"""
        proyectos_sin_calificacion = queryset.filter(calificacion__isnull=True)
        if proyectos_sin_calificacion.exists():
            self.message_user(request, 'No se pueden aprobar proyectos sin calificación', level='error')
            return
        
        updated = queryset.update(estado='aprobado', fecha_revision=timezone.now())
        self.message_user(request, f'{updated} proyecto(s) aprobado(s) exitosamente')
    aprobar_proyectos.short_description = 'Aprobar proyectos seleccionados'
    
    def marcar_en_revision(self, request, queryset):
        """Acción para marcar proyectos en revisión"""
        updated = queryset.update(estado='revisión', fecha_revision=timezone.now())
        self.message_user(request, f'{updated} proyecto(s) marcado(s) en revisión')
    marcar_en_revision.short_description = 'Marcar como en revisión'
