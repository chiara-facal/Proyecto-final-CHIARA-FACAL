from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name="usuario")
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=150)
    pagina_web = models.URLField(null=True, blank=True)
    avatar = models.ImageField(upload_to="avatares", null=True, blank=True)

    @property
    def avatar_url(self):
        return self.avatar.url if self.avatar else ''
    
class Mensaje(models.Model):
    mensaje = models.CharField(max_length=300)
    email = models.EmailField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    para_quien = models.ForeignKey(User, on_delete=models.CASCADE, related_name="destinatario")