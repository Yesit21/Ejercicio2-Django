from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone
from .models import Proyecto

@receiver(pre_save, sender=Proyecto)
def actualizar_fecha_revision(sender, instance, **kwargs):
    """Actualiza la fecha de revisión cuando el estado cambia"""
    if instance.pk:
        try:
            proyecto_anterior = Proyecto.objects.get(pk=instance.pk)
            if proyecto_anterior.estado != instance.estado and instance.estado in ['revisión', 'aprobado']:
                instance.fecha_revision = timezone.now()
        except Proyecto.DoesNotExist:
            pass
