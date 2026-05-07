from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import send_mail
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
            comentario = Comentario.objects.create(
                proyecto=proyecto,
                usuario=request.user,
                texto=form.cleaned_data["texto"],
            )
            destinatario = getattr(proyecto.estudiante, "email", "")
            if destinatario:
                asunto = f"Nuevo comentario en: {proyecto.titulo}"
                mensaje = (
                    f"Proyecto: {proyecto.titulo}\n"
                    f"Usuario que comentó: {request.user.username}\n\n"
                    f"Comentario:\n{comentario.texto}\n"
                )
                try:
                    send_mail(
                        subject=asunto,
                        message=mensaje,
                        from_email=settings.EMAIL_HOST_USER,
                        recipient_list=[destinatario],
                    )
                except Exception:
                    messages.warning(
                        request,
                        "El comentario se guardó, pero no se pudo enviar la notificación por correo.",
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
