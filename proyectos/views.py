from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Proyecto

@login_required
def inicio(request):
    """Vista de inicio con estadísticas para docentes"""
    context = {}
    
    if request.user.groups.filter(name='Docente').exists():
        context['total_proyectos'] = Proyecto.objects.count()
        context['proyectos_revision'] = Proyecto.objects.filter(estado='revisión').count()
        context['proyectos_aprobados'] = Proyecto.objects.filter(estado='aprobado').count()
    
    return render(request, 'proyectos/inicio.html', context)
