from django.apps import AppConfig
# Importamos AppConfig, una clase base que Django usa para configurar aplicaciones.
# Cada aplicación dentro de un proyecto Django puede tener su propia configuración.

class BaseConfig(AppConfig):
    # Creamos una clase de configuración para la aplicación "base".
    # Esta clase permite definir ajustes específicos de la app.

    name = 'base'
    # Nombre de la aplicación. Django usa este valor para identificarla internamente.