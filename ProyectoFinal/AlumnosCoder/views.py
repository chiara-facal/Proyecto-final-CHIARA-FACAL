from django.shortcuts import render
from AlumnosCoder.models import EntradaDeBlog

def index(request):
    posteos = EntradaDeBlog.objects.all()
    return render(request, "AlumnosCoder/index.html", {"posteos": posteos})
