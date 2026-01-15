from django.urls import path
# Importamos la función 'path', que permite definir rutas dentro de la aplicación.

from .views import (
    listaPendientes,
    DetalleTarea,
    CrearTarea,
    EditarTarea,
    EliminarTarea,
    Logueo,
    PaginaRegisrtro
)
# Importamos las vistas basadas en clases (Class-Based Views) que usaremos en las rutas.

from django.contrib.auth.views import LogoutView
# Importamos la vista genérica de Django para cerrar sesión.


urlpatterns = [
    path('', listaPendientes.as_view(), name='tareas'),
    # Ruta principal. Muestra la lista de tareas del usuario.
    # El nombre 'tareas' permite referenciar esta URL desde templates.

    path('registro/', PaginaRegisrtro.as_view(), name='registro'),
    # Página de registro de nuevos usuarios.

    path('login/', Logueo.as_view(), name='login'),
    # Página de inicio de sesión.

    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    # Cerrar sesión. Después de salir, redirige automáticamente a la página de login.

    path('tarea/<int:pk>', DetalleTarea.as_view(), name='tarea'),
    # Vista de detalle de una tarea específica.
    # <int:pk> captura el ID de la tarea desde la URL.

    path('crear-tarea/', CrearTarea.as_view(), name='crear-tarea'),
    # Página para crear una nueva tarea.

    path('editar-tarea/<int:pk>', EditarTarea.as_view(), name='editar-tarea'),
    # Página para editar una tarea existente.

    path('eliminar-tarea/<int:pk>', EliminarTarea.as_view(), name='eliminar-tarea'),
    # Página para confirmar y eliminar una tarea.
]