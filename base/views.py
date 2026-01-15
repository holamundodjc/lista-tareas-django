from django.shortcuts import render, redirect
# Funciones auxiliares para renderizar plantillas y redirigir URLs.

from django.views.generic.list import ListView
# Vista genérica para mostrar listas de objetos.

from django.views.generic.detail import DetailView
# Vista genérica para mostrar el detalle de un solo objeto.

from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
# Vistas genéricas para crear, editar, eliminar y manejar formularios.

from django.contrib.auth.forms import UserCreationForm
# Formulario estándar de Django para registrar nuevos usuarios.

from django.contrib.auth import login
# Función para iniciar sesión manualmente después de registrar un usuario.

from django.contrib.auth.views import LoginView
# Vista genérica para manejar el inicio de sesión.

from django.contrib.auth.mixins import LoginRequiredMixin
# Mixin que obliga a que el usuario esté autenticado para acceder a la vista.

from django.urls import reverse_lazy
# Permite obtener URLs usando el nombre de la ruta, evaluadas de forma diferida.

from base.models import Tarea
# Importamos el modelo Tarea para usarlo en las vistas.


# ------------------------------
# VISTA DE LOGIN
# ------------------------------
class Logueo(LoginView):
    template_name = 'base/login.html'
    # Plantilla que se usará para mostrar el formulario de login.

    fields = '__all__'
    # Indica que se usarán todos los campos del formulario de LoginView.

    redirect_authenticated_user = True
    # Si el usuario ya está autenticado, lo redirige automáticamente.

    def get_success_url(self):
        # Define a qué URL se redirige después de iniciar sesión correctamente.
        return reverse_lazy('tareas')


# ------------------------------
# VISTA DE REGISTRO
# ------------------------------
class PaginaRegisrtro(FormView):
    template_name = 'base/registro.html'
    # Plantilla que muestra el formulario de registro.

    form_class = UserCreationForm
    # Formulario estándar de Django para crear usuarios.

    redirect_authenticated_user = True
    # Si el usuario ya está logueado, no debe ver esta página.

    success_url = reverse_lazy('tareas')
    # URL a la que se redirige después de registrarse correctamente.

    def form_valid(self, form):
        # Se ejecuta cuando el formulario es válido.
        usuario = form.save()  # Crea el usuario en la base de datos.
        if usuario is not None:
            login(self.request, usuario)  # Inicia sesión automáticamente.
        return super(PaginaRegisrtro, self).form_valid(form)

    def get(self, *args, **kwargs):
        # Si el usuario ya está autenticado, lo enviamos a la lista de tareas.
        if self.request.user.is_authenticated:
            return redirect('tareas')
        return super(PaginaRegisrtro, self).get(*args, **kwargs)


# ------------------------------
# LISTA DE TAREAS
# ------------------------------
class listaPendientes(LoginRequiredMixin, ListView):
    model = Tarea
    # Modelo que se va a listar.

    context_object_name = 'tareas'
    # Nombre con el que se accederá a la lista en la plantilla.

    def get_context_data(self, **kwargs):
        # Agrega datos adicionales al contexto enviado a la plantilla.
        context = super().get_context_data(**kwargs)

        # Filtra las tareas para mostrar solo las del usuario actual.
        context['tareas'] = context['tareas'].filter(usuarios=self.request.user)

        # Cuenta cuántas tareas están incompletas.
        context['count'] = context['tareas'].filter(completo=False).count()

        # Captura el valor buscado desde el formulario GET.
        valor_buscado = self.request.GET.get('area-buscar') or ''

        # Si hay texto de búsqueda, filtra por título.
        if valor_buscado:
            context['tareas'] = context['tareas'].filter(titulo__icontains=valor_buscado)

        # Mantiene el valor buscado en el input.
        context['valor_buscado'] = valor_buscado

        return context


# ------------------------------
# DETALLE DE UNA TAREA
# ------------------------------
class DetalleTarea(LoginRequiredMixin, DetailView):
    model = Tarea
    # Modelo del cual se mostrará un solo objeto.

    context_object_name = 'tarea'
    # Nombre con el que se accede al objeto en la plantilla.

    template_name = 'base/tarea.html'
    # Plantilla personalizada para mostrar el detalle.


# ------------------------------
# CREAR UNA TAREA
# ------------------------------
class CrearTarea(LoginRequiredMixin, CreateView):
    model = Tarea
    # Modelo que se va a crear.

    fields = ['titulo', 'descripcion', 'completo']
    # Campos que se mostrarán en el formulario.

    success_url = reverse_lazy('tareas')
    # Redirección después de crear la tarea.

    def form_valid(self, form):
        # Asigna automáticamente el usuario actual a la tarea creada.
        form.instance.usuarios = self.request.user
        return super(CrearTarea, self).form_valid(form)


# ------------------------------
# EDITAR UNA TAREA
# ------------------------------
class EditarTarea(LoginRequiredMixin, UpdateView):
    model = Tarea
    # Modelo que se va a editar.

    fields = ['titulo', 'descripcion', 'completo']
    # Campos editables.

    success_url = reverse_lazy('tareas')
    # Redirección después de editar.


# ------------------------------
# ELIMINAR UNA TAREA
# ------------------------------
class EliminarTarea(LoginRequiredMixin, DeleteView):
    model = Tarea
    # Modelo que se va a eliminar.

    context_object_name = 'tarea'
    # Nombre del objeto en la plantilla.

    success_url = reverse_lazy('tareas')
    # Redirección después de eliminar.