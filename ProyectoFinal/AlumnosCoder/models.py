from django.db import models

class EntradaDeBlog(models.Model):
    titulo_entrada = models.CharField(max_length=50)
    subtitulo_entrada= models.CharField (max_length = 30)
    descripcion = models.CharField (max_length = 200)
    fecha_creacion = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return f' {self.titulo_entrada} - {self.subtitulo_entrada} '