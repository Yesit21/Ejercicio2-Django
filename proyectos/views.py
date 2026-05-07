import csv

from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
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

@login_required
def exportar_proyectos_csv(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="proyectos.csv"'

    writer = csv.writer(response)
    writer.writerow(["Título", "Estado", "Estudiante", "Fecha de envío", "Calificación"])

    proyectos = Proyecto.objects.select_related("estudiante").all()
    for proyecto in proyectos:
        writer.writerow(
            [
                proyecto.titulo,
                proyecto.estado,
                proyecto.estudiante.username,
                proyecto.fecha_envio,
                proyecto.calificacion if proyecto.calificacion is not None else "",
            ]
        )

    return response


class ProyectoListView(LoginRequiredMixin, ListView):
    model = Proyecto
    template_name = 'proyectos/proyecto_list.html'
    context_object_name = 'proyectos'

    def get_queryset(self):
        queryset = super().get_queryset().select_related('estudiante')

        estado = self.request.GET.get('estado')
        if estado:
            queryset = queryset.filter(estado=estado)

        estudiante = self.request.GET.get('estudiante')
        if estudiante and estudiante.isdigit():
            queryset = queryset.filter(estudiante_id=int(estudiante))

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        User = get_user_model()
        context['estados'] = Proyecto.ESTADOS
        context['estudiantes'] = (
            User.objects.filter(proyectos__isnull=False)
            .distinct()
            .order_by('username')
        )
        context['estado_seleccionado'] = self.request.GET.get('estado', '')
        context['estudiante_seleccionado'] = self.request.GET.get('estudiante', '')

        return context


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
