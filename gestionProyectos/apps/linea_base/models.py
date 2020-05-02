from django.db import models

# Create your models here.
class LineaBase(models.Model):
    linea_base = models.CharField(max_length=70)
    ESTADO_LB = (
        ('Iniciado', 'Iniciado'),
        ('Pendiente', 'Pendiente'),
    )
    estado = models.CharField(max_length=12, default='Pendiente', choices=ESTADO_LB)
    
    def __str__ (self):
        return '{}'.format(self.linea_base)