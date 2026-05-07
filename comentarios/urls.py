from django.urls import path

from . import views

app_name = 'comentarios'

urlpatterns = [
    path('proyecto/<int:proyecto_id>/comentar/', views.crear_comentario, name='crear_comentario'),
]
