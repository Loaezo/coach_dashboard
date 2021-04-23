# Aquí me deja usar el login con el nombre del usario, pero vamos a sobreescribirlo para poder hacer login con el email
from django.db import models

# es la clase básica de usuario que vamos a usar
from django.contrib.auth.models import AbstractBaseUser

from django.contrib.auth.models import PermissionsMixin

# (1) importamos de aquí mismo el base user manager
from django.contrib.auth.models import BaseUserManager

class UserPRofileManager(BaseUserManager):
    """ Manager para perfiles de usuario """
    # La forma en la que los managers funcionan es que especificas funciones para poder manipular lo que se tiene adentro de user profile
def create_user(self, email, name, password=None):
    """ Crear nuevo usuer profile """
    if not email:
        raise ValueError ('El usuario debe tener un email')
    
    email = self.normalize_email(email)
    user = self.model(email=email, name=name)

    user.ser_password(password)
    user.save(using=self_db)

    return user

def create_superuser(self, email, name, password):
    user = self.create_user(email, name, password)

    user.is_superuser = True
    user.is_staff = True
    user.save(using=self._db)



class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ Modelo de la DB para Usuarios en el sistema """
    email = models.EmailField(max_length=255, unique=True) 
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # Ahora vamos a especificar el model manager que vamos a usar para nuestros objetos

    # Esto es requerido porque tenemos que usar nuestro modelo de Django personalizado con el Django CLI, la línea de comandos de Django
    # Django necesita un custom user manager para que sepa cómo GRUD a los usuarios

    # a este objeto vamos a llamarlo objects

    objects = UserProfileManager()

    # Definimos en username_field el campo de login que el usuario va a especificar
    USERNAME_FIELD = 'email'
    # qué campos serán requeridos?
    REQUIRED_FIELDS = ['name']  
    # definimos 2 funciones para poder llamar el nombre para ver el nombre como string, podemos llamar a esta clase
     def get_full_name(self):
         return self.name
         """Obtiener el nombre completo del Usuario"""
    # no tenemos otra manera de definir el short name, lo dejamos como name, sólo para tenerreferencia al nombre cuando querramos acceder desed otro lugar
     def get_short_name(self):
         """Obtener el nombre corto del Usuario"""
         return self.name
    # querermos mostrar la representación en string de nuestro modelo:
    def __str__(self):
        """Obtener cadena representando al Usuario"""
        return self.email
    # Vamos a crear un manager para poder trabajar con este modelo. Debido a que tenemos un modelo de usuario personalizado, necesitamos especificar cómo vasmo a procesar a los usuarios, nos vamos a models.py. Ir a (1)
