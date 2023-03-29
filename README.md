# Proyecto-final-CHIARA-FACAL

Proyecto final del curso de Python de CoderHouse. Realizado por Chiara Facal

**Cosas que realicé**

- creé un proyecto en Django, con dos aplicaciones, una para la creación/edición/borrado de posts y otra para la creación del usuario y la mensajería
- incluye verificación de usuario donde solamente quienes estén registrados van a poder crear/editar y borrar sus posts
- Adicionalmente, se verifica que solo aquel que creó el post pueda alterarlo
- Luego de cada alumno registrarse, este puede modificar su usuario, agregando incluso una foto de perfil, y mandar/recibir mensajes de otros usuarios
- Existe un panel de administración, donde aquel que esté logueado como administrador podrá administrar los posts, los usuarios y los mensajes creados

**Paquetes necesarios para la instalación**

Desde la terminal correr el siguiente comando

```
pip3 install django
```

**Cargar datos de pruebas**

Para terminal bash en windows/linux/macos:

```
python3 manage.py shell < seed_data.py
```

Para terminal cmd/powershell en windows: Primero entrar al shell de django con

```
python3 manage.py shell
```

Una vez en el shell hacer import seed_data

```
Python 3.11.2 (v3.11.2:878ead1ac1, Feb  7 2023, 10:02:41) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> import seed_data
```

**Para poder correr el servidor**

Desde la terminal correr el siguiente comando

```
python3 manage.py runserver
```
