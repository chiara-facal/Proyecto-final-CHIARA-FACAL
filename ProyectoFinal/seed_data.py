from AlumnosCoder.models import EntradaDeBlog
from PerfilMensaje.models import Perfil, Mensaje

EntradaDeBlog(titulo_entrada = "titulo1",
subtitulo_entrada = "subtitulo1",
descripcion = "descripcion1"
).save()

EntradaDeBlog(titulo_entrada = "titulo2",
subtitulo_entrada = "subtitulo2",
descripcion = "descripcion2"
).save()

EntradaDeBlog(titulo_entrada = "titulo3",
subtitulo_entrada = "subtitulo3",
descripcion = "descripcion3"
).save()

Perfil(nombre ="nombre1",
descripcion = "descripcion1"
).save()

Perfil(nombre ="nombre2",
descripcion = "descripcion2"
).save()

Perfil(nombre ="nombre3",
descripcion = "descripcion3"
).save()
