from django.contrib import admin
# Importamos el módulo 'admin' de Django, que permite administrar modelos
# desde el panel de administración integrado.

from .models import Tarea
# Importamos el modelo 'Tarea' desde el archivo models.py del mismo directorio.
# Esto permite que el modelo pueda ser registrado en el panel de administración.

admin.site.register(Tarea)
# Registramos el modelo 'Tarea' en el sitio de administración de Django.
# Esto hace que aparezca en el panel admin y podamos crear, editar y eliminar tareas desde ahí.
