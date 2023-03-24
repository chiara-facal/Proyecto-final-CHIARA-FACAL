from django.shortcuts import render
from AlumnosCoder.models import EntradaDeBlog
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def index(request):
    posteos = EntradaDeBlog.objects.all()
    return render(request, "AlumnosCoder/index.html", {"posteos": posteos})

class Entradalist(ListView):
    model = EntradaDeBlog
    context_object_name = "entradas"

class Mispost(LoginRequiredMixin, Entradalist):
    def get_queryset(self):
        return EntradaDeBlog.objects.filter(editor=self.request.user.id).all()
    
class Detalle(DetailView):
    model = EntradaDeBlog
    context_object_name = "entrada"

class Actualizar(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = EntradaDeBlog
    success_url = reverse_lazy('entradadeblog_list')
    fields = '__all__'

    def test_func(self):
        usuario_id = self.request.user.id
        entrada_id =  self.kwargs.get("pk")
        return EntradaDeBlog.objects.filter(editor=usuario_id, id=entrada_id).exists()
    
class Borrar(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = EntradaDeBlog
    context_object_name = "entrada"
    success_url = reverse_lazy('entradadeblog_list')

    def test_func(self):
        usuario_id = self.request.user.id
        entrada_id =  self.kwargs.get("pk")
        return EntradaDeBlog.objects.filter(editor=usuario_id, id=entrada_id).exists()

class Registro(CreateView):
    form_class = UserCreationForm
    template_name = "registro/registro.html"
    success_url = reverse_lazy('entradadeblog_list')

class Ingresar(LoginView):
    next_page = reverse_lazy("inicio")
    template_name = "registro/ingresar.html"

class Salir(LogoutView):
    template_name = "registro/salir.html"