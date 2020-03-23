from django import forms
from apps.proyecto.models import Proyecto

class ProyectoForm (forms.ModelForm):
	class Meta:
		model = Proyecto

		fields = [
			'nombre_proyecto', 			
		]
		
		labels = {
			'nombre_proyecto': 'Nombre del Proyecto'
		}
		
		widgets = {
			'nombre_proyecto': forms.TextInput(attrs={'class':'form-control'}),
		}