from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from proyectos.models import Proyecto

from .forms import ComentarioForm
from .models import Comentario


@login_required
def crear_comentario(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, pk=proyecto_id)

    if proyecto.estado == "aprobado":
        messages.error(request, "No puedes comentar en un proyecto aprobado.")
        return redirect("proyectos:proyecto_detail", pk=proyecto.pk)

    if request.method == "POST":
        form = ComentarioForm(request.POST)
        if form.is_valid():
            Comentario.objects.create(
                proyecto=proyecto,
                usuario=request.user,
                texto=form.cleaned_data["texto"],
            )
            messages.success(request, "Comentario agregado correctamente.")
            return redirect("proyectos:proyecto_detail", pk=proyecto.pk)

        messages.error(request, "No se pudo guardar el comentario. Revisa el texto.")
    else:
        form = ComentarioForm()

    return render(
        request,
        "proyectos/proyecto_detail.html",
        {"proyecto": proyecto, "form": form},
    )
