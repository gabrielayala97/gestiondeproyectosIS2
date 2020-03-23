from django.db import models

# Create your models here.
class Proyecto(models.Model):

	nombre_proyecto = models.CharField(max_length=70)
	

	def __str__ (self):
		return '{}'.format(self.nombre_proyecto)