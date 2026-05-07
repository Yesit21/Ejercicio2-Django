from django.core.exceptions import PermissionDenied


class SoloDuenoMixin:

    def dispatch(self, request, *args, **kwargs):

        proyecto = self.get_object()

        if proyecto.estudiante != request.user:
            raise PermissionDenied

        if proyecto.estado == 'aprobado':
            raise PermissionDenied

        return super().dispatch(request, *args, **kwargs)


class SoloEstudiantesMixin:

    def dispatch(self, request, *args, **kwargs):

        if not request.user.groups.filter(
            name='Estudiantes'
        ).exists():

            raise PermissionDenied

        return super().dispatch(request, *args, **kwargs)
    