from django.db import models
from apps.proyecto.models import Proyecto
from apps.linea_base.models import LineaBase

# Create your models here.
class Tarea(models.Model):
	version = models.CharField(max_length=10)
	descripcion = models.CharField(max_length=50)
	observacion = models.CharField(max_length=200, null=True)
	id_tarea_padre = models.OneToOneField('self', null=True, blank=True, on_delete=models.CASCADE)
	proyecto = models.ForeignKey(Proyecto, null=True, blank=True, on_delete=models.CASCADE)
	
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
	linea_base = models.ForeignKey(LineaBase, null=True, blank=True, on_delete=models.SET_NULL)

	def __str__ (self):
			return '{}'.format(self.id)