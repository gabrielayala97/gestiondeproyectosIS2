from django.db import models
from apps.usuario.models import Usuario

# Create your models here.
class Rol(models.Model):
	nombre_rol = models.CharField(max_length=50)
	def __str__ (self):
		return '{}'.format(self.nombre_rol)	

	
class Usuario_Posee_Rol(models.Model):
	usuario = models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.CASCADE)
	rol = models.ForeignKey(Rol, null=True, blank=True, on_delete=models.CASCADE)