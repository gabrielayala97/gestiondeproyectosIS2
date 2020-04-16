from django.db import models
from apps.usuario.models import Usuario

# Create your models here.
class Proyecto(models.Model):
	nombre_proyecto = models.CharField(max_length=70)
	usuarios = models.ManyToManyField(Usuario, blank=True)

	def __str__ (self):
		return '{}'.format(self.nombre_proyecto)