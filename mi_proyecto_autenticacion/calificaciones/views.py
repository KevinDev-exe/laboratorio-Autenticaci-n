from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Calificacion
from django.db.models import Avg

#  PROTECCIÓN LOGIN
from django.contrib.auth.mixins import LoginRequiredMixin

#  REGISTRO
from .forms import RegistroForm
from django.shortcuts import render, redirect


# 👉 REDIRECCIÓN INICIAL (cuando entran a "/")
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

@login_required
def inicio(request):
    return redirect('listar')


#  REGISTRO DE USUARIO
def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistroForm()

    return render(request, 'registro.html', {'form': form})


#  LISTAR
class ListaCalificaciones(LoginRequiredMixin, ListView):
    model = Calificacion
    template_name = 'calificaciones/listar.html'

    def get_queryset(self):
        return Calificacion.objects.filter(usuario=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['promedio_general'] = Calificacion.objects.filter(
            usuario=self.request.user
        ).aggregate(Avg('promedio'))['promedio__avg']
        return context


#  CREAR
class CrearCalificacion(LoginRequiredMixin, CreateView):
    model = Calificacion
    fields = ['nombre_estudiante','identificacion','asignatura','nota1','nota2','nota3']
    template_name = 'calificaciones/crear.html'
    success_url = reverse_lazy('listar')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)


#  EDITAR
class EditarCalificacion(LoginRequiredMixin, UpdateView):
    model = Calificacion
    fields = ['nombre_estudiante','identificacion','asignatura','nota1','nota2','nota3']
    template_name = 'calificaciones/editar.html'
    success_url = reverse_lazy('listar')

    def get_queryset(self):
        return Calificacion.objects.filter(usuario=self.request.user)


#  ELIMINAR
class EliminarCalificacion(LoginRequiredMixin, DeleteView):
    model = Calificacion
    template_name = 'calificaciones/eliminar.html'
    success_url = reverse_lazy('listar')

    def get_queryset(self):
        return Calificacion.objects.filter(usuario=self.request.user)
    

from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.models import User
from django.contrib import messages

class CustomPasswordResetView(PasswordResetView):
    template_name = 'password_reset.html'

    def form_valid(self, form):
        email = form.cleaned_data['email']

        if not User.objects.filter(email=email).exists():
            messages.error(self.request, '❌ Este correo no está registrado')
            return self.form_invalid(form)

        messages.success(self.request, '✔ Se envió el correo correctamente')
        return super().form_valid(form)