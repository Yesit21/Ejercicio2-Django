from django.urls import path
from django.views.generic import TemplateView

app_name = 'proyectos'

urlpatterns = [
    # Vista temporal de inicio
    path('', TemplateView.as_view(template_name='proyectos/inicio.html'), name='inicio'),
]
