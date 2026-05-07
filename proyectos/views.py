from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from .models import Proyecto
from .forms import (
    ProyectoForm,
    ProyectoUpdateForm
)
from .permisos import (
    SoloDuenoMixin,
    SoloEstudiantesMixin
)


@login_required
def inicio(request):
    """Vista de inicio con estadísticas para docentes"""
    context = {}
    
    if request.user.groups.filter(name='Docente').exists():
        context['total_proyectos'] = Proyecto.objects.count()
        context['proyectos_revision'] = Proyecto.objects.filter(estado='revision').count()
        context['proyectos_aprobados'] = Proyecto.objects.filter(estado='aprobado').count()
    
    return render(request, 'proyectos/inicio.html', context)


class ProyectoListView(LoginRequiredMixin, ListView):
    model = Proyecto
    template_name = 'proyectos/proyecto_list.html'
    context_object_name = 'proyectos'


class ProyectoDetailView(LoginRequiredMixin, DetailView):
    model = Proyecto
    template_name = 'proyectos/proyecto_detail.html'


class ProyectoCreateView(LoginRequiredMixin, SoloEstudiantesMixin, CreateView):
    model = Proyecto
    form_class = ProyectoForm
    template_name = 'proyectos/proyecto_form.html'

    def form_valid(self, form):
        form.instance.estudiante = self.request.user
        messages.success(self.request, 'Proyecto creado correctamente')
        return super().form_valid(form)


class ProyectoUpdateView(LoginRequiredMixin, SoloDuenoMixin, UpdateView):
    model = Proyecto
    form_class = ProyectoUpdateForm
    template_name = 'proyectos/proyecto_form.html'

    def form_valid(self, form):
        messages.success(self.request, 'Proyecto actualizado')
        return super().form_valid(form)


class ProyectoDeleteView(LoginRequiredMixin, SoloDuenoMixin, DeleteView):
    model = Proyecto
    template_name = 'proyectos/proyecto_confirm_delete.html'
    success_url = reverse_lazy('proyecto_list')

    def form_valid(self, form):
        messages.success(self.request, 'Proyecto eliminado')
        return super().form_valid(form)
