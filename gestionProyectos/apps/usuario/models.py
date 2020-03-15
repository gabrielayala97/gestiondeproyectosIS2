from django.db import models



# Create your models here.

class Usuario(models.Model):
	nombre = models.CharField(max_length=50)
	apellido = models.CharField(max_length=50)
	email = models.EmailField(max_length=50)
	user_name = models.CharField(max_length=50)
	password = models.CharField(max_length=50)

	def __str__ (self):
		return '{}'.format(self.nombre)

	
        
	    