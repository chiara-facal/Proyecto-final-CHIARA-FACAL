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
from AlumnosCoder.views import index, Entradalist, Registro, Ingresar, Salir, Mispost, Detalle, Actualizar, Borrar, Crear, BuscarEntrada
from PerfilMensaje.views import CrearPerfil, ActualizarPerfil
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="inicio"),
    path('entradas/listado', Entradalist.as_view(), name = "entradadeblog_list"),
    path('entradas/mis-entradas', Mispost.as_view(), name = "mis_posts"),
    path('entrada/<pk>/detalle', Detalle.as_view(), name = "entrada_detalle"),
    path('entrada/<pk>/editar',Actualizar.as_view(), name="actualizar_entrada"),
    path('entrada/<pk>/borrar', Borrar.as_view(), name = "borrar_entrada"),
    path('entrada/crear', Crear.as_view(), name = "crear_entrada" ),
    path('entrada/buscar', BuscarEntrada.as_view(), name = "buscar_entrada"),
    path('usuario/registro', Registro.as_view(), name = "registro"),
    path('usuario/ingresar', Ingresar.as_view(), name = "ingresar"),
    path('usuario/salir', Salir.as_view(), name = "salir"),
    path('perfil/crear', CrearPerfil.as_view(), name = "crear_perfil"),
    path('perfil/<pk>/actualizar', ActualizarPerfil.as_view(), name = "actualizar_perfil"),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)