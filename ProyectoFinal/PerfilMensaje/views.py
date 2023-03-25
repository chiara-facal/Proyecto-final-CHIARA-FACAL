from django.shortcuts import render
from PerfilMensaje.models import Perfil
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class CrearPerfil(LoginRequiredMixin, CreateView):
    model = Perfil
    success_url = reverse_lazy('entradadeblog_list')
    fields = ['nombre', 'descripcion', 'pagina_web', 'avatar']

    def form_valid(self,form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)
    
class ActualizarPerfil(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Perfil
    success_url = reverse_lazy('entradadeblog_list')
    fields = ['nombre', 'descripcion', 'pagina_web', 'avatar']

    def test_func(self):
        return Perfil.objects.filter(usuario=self.request.user).exists

