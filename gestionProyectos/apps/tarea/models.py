from django.db import models

# Create your models here.
class Tarea(models.Model):
	version = models.CharField(max_length=10)
	descripcion = models.CharField(max_length=50)
	observacion = models.CharField(max_length=200, null=True)
	id_tarea_padre = models.IntegerField(null=True)

	PRIORIDAD_TAREA = (
        ('Alta', 'Alta'),
        ('Baja', 'Baja'),
        ('Normal', 'Normal'),
    )
	prioridad = models.CharField(max_length=10, choices=PRIORIDAD_TAREA)

	ESTADOS_TAREA = (
        ('Iniciado', 'Iniciado'),
        ('Pendiente', 'Pendiente'),
        ('Finalizado', 'Finalizado'),
    )
	estado = models.CharField(max_length=15, choices=ESTADOS_TAREA)	

	def __str__ (self):
			return '{}'.format(self.descripcion)