from django.db import models
#from apps.usuario.models import Usuario
from django.contrib import admin
#from apps.permiso.models import Permiso

# Create your models here.
class Rol(models.Model):
	nombre_rol= models.CharField(max_length=50)
	#permiso = models.OneToOneField(Permiso,null=True, blank=True, on_delete=models.CASCADE)

	PERMISO_ROL = (
        ('administracion', 'Administracion'),
        ('desarrollo', 'Desarrollo'),
        ('configuracion', 'Configuracion'),
    )
	permiso = models.CharField(max_length=14, choices=PERMISO_ROL)

	def __str__ (self):
		return '{}'.format(self.nombre_rol, self.permiso)

@admin.register(Rol)
class RolAdmin(admin.ModelAdmin):
    pass
	
""""class Usuario_Posee_Rol(models.Model):
	usuario = models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.CASCADE)
	rol = models.ForeignKey(Rol, null=True, blank=True, on_delete=models.CASCADE)"""

