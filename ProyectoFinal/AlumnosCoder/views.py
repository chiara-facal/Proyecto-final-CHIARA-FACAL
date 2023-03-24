from django.shortcuts import render
from AlumnosCoder.models import EntradaDeBlog
from django.views.generic import ListView

def index(request):
    posteos = EntradaDeBlog.objects.all()
    return render(request, "AlumnosCoder/index.html", {"posteos": posteos})

class Entradalist(ListView):
    model = EntradaDeBlog
    context_object_name = "entradas"

