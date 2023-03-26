from django.shortcuts import render
from PerfilMensaje.models import Perfil, Mensaje
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
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
        return Perfil.objects.filter(usuario=self.request.user).exists()
    
class CrearMensaje(CreateView):
    model = Mensaje
    success_url = reverse_lazy("crear_mensaje")
    fields = "__all__"

class BorrarMensaje(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Mensaje
    context_object_name = "mensaje"
    success_url = reverse_lazy("lista_mensajes")

    def test_func(self):
        return Mensaje.objects.filter(para_quien=self.request.user).exists()

class ListaMensaje(LoginRequiredMixin, ListView):
    model = Mensaje
    context_object_name = "mensajes"
    def get_queryset(self):
        import pdb; pdb.set_trace
        return Mensaje.objects.filter(para_quien=self.request.user).all()
    

