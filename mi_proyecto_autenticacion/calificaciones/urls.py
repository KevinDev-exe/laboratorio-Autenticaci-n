from django.urls import path
from .views import *

urlpatterns = [
    path('', ListaCalificaciones.as_view(), name='listar'),
    path('crear/', CrearCalificacion.as_view(), name='crear'),
    path('editar/<int:pk>/', EditarCalificacion.as_view(), name='editar'),
    path('eliminar/<int:pk>/', EliminarCalificacion.as_view(), name='eliminar'),
]