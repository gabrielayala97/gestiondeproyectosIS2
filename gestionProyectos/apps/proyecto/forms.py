from django import forms
from apps.proyecto.models import Proyecto

class ProyectoForm (forms.ModelForm):
	class Meta:
		model = Proyecto

		fields = [
			'nombre_proyecto',
			'usuarios',
		]
		
		labels = {
			'nombre_proyecto': 'Nombre del Proyecto',
			'usuarios': 'Usuarios',
		}
		
		widgets = {
			'nombre_proyecto': forms.TextInput(attrs={'class':'form-control'}),
			'usuarios': forms.CheckboxSelectMultiple(),
		}