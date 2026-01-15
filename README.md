# Lista de Tareas en Django

Aplicación web desarrollada con Django que permite a los usuarios registrarse, iniciar sesión y gestionar sus tareas personales. Incluye CRUD completo, autenticación, filtrado y búsqueda de tareas.

## Características

- Registro de usuarios con formulario estándar de Django.
- Inicio de sesión y cierre de sesión con autenticación integrada.
- CRUD completo de tareas (crear, leer, actualizar y eliminar).
- Cada usuario solo puede ver sus propias tareas.
- Búsqueda de tareas por título.
- Contador de tareas pendientes.
- Interfaz simple y funcional basada en plantillas HTML.

## Requisitos

- Python 3.10 o superior
- pip (gestor de paquetes de Python)
- Entorno virtual recomendado

## Instalación

1. Clonar el repositorio:

   git clone https://github.com/holamundodjc/lista-tareas-django.git

2. Entrar al directorio del proyecto:

   cd lista-tareas-django

3. Crear un entorno virtual:

   python -m venv venv

4. Activar el entorno virtual:

   - Windows:
     venv\Scripts\activate

   - Linux/Mac:
     source venv/bin/activate

5. Instalar las dependencias:

   pip install -r requirements.txt

6. Aplicar las migraciones:

   python manage.py migrate

7. Ejecutar el servidor:

   python manage.py runserver

8. Abrir la aplicación en el navegador:

   http://127.0.0.1:8000/

## Tecnologías utilizadas

- Python 3
- Django 4
- HTML y CSS
- SQLite (base de datos por defecto de Django)
- Entorno virtual de Python (venv)
- Git y GitHub para control de versiones

## Capturas de pantalla

### Página de inicio
![Home](ruta/a/tu/imagen1.png)

### Lista de tareas
![Lista de tareas](ruta/a/tu/imagen2.png)

### Formulario de creación/edición
![Formulario](ruta/a/tu/imagen3.png)

### Pantalla de login
![Login](ruta/a/tu/imagen4.png)

## Licencia

Este proyecto está bajo la licencia MIT. Puedes usar, modificar y distribuir este software libremente, siempre que se mantenga el aviso de copyright.