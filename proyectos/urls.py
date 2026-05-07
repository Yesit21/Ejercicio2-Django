from django.urls import path

from .views import (
    ProyectoListView,
    ProyectoDetailView,
    ProyectoCreateView,
    ProyectoUpdateView,
    ProyectoDeleteView
)

urlpatterns = [

    path(
        '',
        ProyectoListView.as_view(),
        name='proyecto_list'
    ),

    path(
        'crear/',
        ProyectoCreateView.as_view(),
        name='proyecto_create'
    ),

    path(
        '<int:pk>/',
        ProyectoDetailView.as_view(),
        name='proyecto_detail'
    ),

    path(
        '<int:pk>/editar/',
        ProyectoUpdateView.as_view(),
        name='proyecto_update'
    ),

    path(
        '<int:pk>/eliminar/',
        ProyectoDeleteView.as_view(),
        name='proyecto_delete'
    ),

    path('usuarios/', include('usuarios.urls')),
]