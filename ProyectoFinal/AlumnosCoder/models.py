from django.db import models
from django.contrib.auth.models import User

class EntradaDeBlog(models.Model):
    titulo_entrada = models.CharField(max_length=50)
    subtitulo_entrada= models.CharField (max_length = 30)
    descripcion = models.CharField (max_length = 200)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    editor = models.ForeignKey(to=User,on_delete=models.CASCADE,default = 1,related_name="editor")
    imagen = models.ImageField(upload_to="entradas", null=True, blank=True)

    @property
    def imagen_url(self):
        return self.imagen.url if self.imagen else ''


    def __str__(self):
        return f"{self.id} - {self.carousel_caption_title}"

    def __str__(self):
        return f' {self.titulo_entrada} - {self.subtitulo_entrada} '