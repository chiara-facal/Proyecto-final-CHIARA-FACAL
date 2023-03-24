"""ProyectoFinal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from AlumnosCoder.views import index, Entradalist, Registro, Ingresar, Salir
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="inicio"),
    path('entradas/listado', Entradalist.as_view(), name = "entradadeblog_list"),
    path('usuario/registro', Registro.as_view(), name = "registro"),
    path('usuario/ingresar', Ingresar.as_view(), name = "ingresar"),
    path('usuario/salir', Salir.as_view(), name = "salir"),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)