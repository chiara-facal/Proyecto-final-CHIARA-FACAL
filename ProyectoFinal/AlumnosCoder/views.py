from django.shortcuts import render
from AlumnosCoder.models import EntradaDeBlog
from django.views.generic import ListView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView

def index(request):
    posteos = EntradaDeBlog.objects.all()
    return render(request, "AlumnosCoder/index.html", {"posteos": posteos})

class Entradalist(ListView):
    model = EntradaDeBlog
    context_object_name = "entradas"

class Registro(CreateView):
    form_class = UserCreationForm
    template_name = "registro/registro.html"
    success_url = reverse_lazy('entradadeblog_list')

class Ingresar(LoginView):
    next_page = reverse_lazy("inicio")
    template_name = "registro/ingresar.html"

class Salir(LogoutView):
    template_name = "registro/salir.html"