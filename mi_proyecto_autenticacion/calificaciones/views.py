from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Calificacion
from django.db.models import Avg

class ListaCalificaciones(ListView):
    model = Calificacion
    template_name = 'calificaciones/listar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['promedio_general'] = Calificacion.objects.aggregate(Avg('promedio'))['promedio__avg']
        return context


class CrearCalificacion(CreateView):
    model = Calificacion
    fields = ['nombre_estudiante','identificacion','asignatura','nota1','nota2','nota3']
    template_name = 'calificaciones/crear.html'
    success_url = reverse_lazy('listar')


class EditarCalificacion(UpdateView):
    model = Calificacion
    fields = ['nombre_estudiante','identificacion','asignatura','nota1','nota2','nota3']
    template_name = 'calificaciones/editar.html'
    success_url = reverse_lazy('listar')


class EliminarCalificacion(DeleteView):
    model = Calificacion
    template_name = 'calificaciones/eliminar.html'
    success_url = reverse_lazy('listar')