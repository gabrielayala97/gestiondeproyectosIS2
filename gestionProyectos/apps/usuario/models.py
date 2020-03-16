from django.db import models

#from apps.rol.models import Rol

# Create your models here.

class Usuario(models.Model):
	nombre = models.CharField(max_length=50)
	apellido = models.CharField(max_length=50)
	email = models.EmailField(max_length=50)
	username = models.CharField(max_length=50)
	password = models.CharField(max_length=50)

	def __str__ (self):
			return '{}'.format(self.nombre)
#	roles = models.ForeignKey(Rol, null=True, blank=True, on_delete=models.CASCADE)
	#def __str__ (self):
	#	return self.nombre+self.apellido+self.email+self.password