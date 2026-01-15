from django.db import models
# Importamos el módulo 'models' de Django, que contiene todas las clases base
# necesarias para definir modelos (tablas) en la base de datos.

from django.contrib.auth.models import User
# Importamos el modelo 'User' que viene incluido en Django.
# Esto permite relacionar cada tarea con un usuario del sistema.


class Tarea(models.Model):
    # Definimos el modelo 'Tarea', que representará una tabla en la base de datos.

    usuarios = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    # Relación de muchos-a-uno con el modelo User.
    # Cada tarea pertenece a un usuario.
    # on_delete=models.CASCADE → si el usuario se elimina, sus tareas también.
    # null=True → permite que el campo quede vacío en la base de datos.
    # blank=True → permite que el campo quede vacío en formularios.

    titulo = models.CharField(max_length=200)
    # Campo de texto corto para el título de la tarea.
    # max_length define el límite de caracteres.

    descripcion = models.TextField(
        null=True,
        blank=True
    )
    # Campo de texto largo para la descripción de la tarea.
    # null=True y blank=True permiten que sea opcional.

    completo = models.BooleanField(default=False)
    # Campo booleano que indica si la tarea está completada.
    # Por defecto, todas las tareas se crean como incompletas.

    creado = models.DateTimeField(auto_now_add=True)
    # Fecha y hora en que se creó la tarea.
    # auto_now_add=True hace que Django registre automáticamente el momento de creación.


    def __str__(self):
        return self.titulo
    # Método que define cómo se mostrará la tarea como texto.
    # Muy útil en el panel de administración y en el shell.


    class Meta:
        ordering = ['completo']
    # Configuración adicional del modelo.
    # 'ordering' define el orden por defecto al consultar tareas:
    # primero las incompletas (False), luego las completas (True).