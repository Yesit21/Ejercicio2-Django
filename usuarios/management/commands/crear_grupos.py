from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group

class Command(BaseCommand):
    help = 'Crea los grupos Estudiante y Docente'

    def handle(self, *args, **kwargs):
        grupos = ['Estudiante', 'Docente']
        
        for nombre_grupo in grupos:
            grupo, created = Group.objects.get_or_create(name=nombre_grupo)
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Grupo "{nombre_grupo}" creado exitosamente')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'El grupo "{nombre_grupo}" ya existe')
                )
        
        self.stdout.write(
            self.style.SUCCESS('\n✅ Proceso completado')
        )
