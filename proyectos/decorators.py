from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import PermissionDenied
from functools import wraps

def estudiante_required(view_func):
    """Decorador que verifica si el usuario pertenece al grupo Estudiante"""
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.user.groups.filter(name='Estudiante').exists():
            return view_func(request, *args, **kwargs)
        raise PermissionDenied
    return wrapper

def docente_required(view_func):
    """Decorador que verifica si el usuario pertenece al grupo Docente"""
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.user.groups.filter(name='Docente').exists():
            return view_func(request, *args, **kwargs)
        raise PermissionDenied
    return wrapper

def grupo_required(*grupos):
    """Decorador genérico que verifica si el usuario pertenece a alguno de los grupos especificados"""
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            if request.user.groups.filter(name__in=grupos).exists():
                return view_func(request, *args, **kwargs)
            raise PermissionDenied
        return wrapper
    return decorator
