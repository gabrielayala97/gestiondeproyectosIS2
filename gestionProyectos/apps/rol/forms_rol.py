from django import forms
from .models import Rol,Usuario_Posee_Rol

class RolForm (forms.ModelForm):
	class Meta:
		model = Rol
		
		fields = [
			'nombre_rol',
		]
		
		labels = {
			'nombre_rol': 'Nombre del Rol',
		}
		
		widgets = {
			'nombre_rol': forms.TextInput(attrs={'class':'form-control'}),
		}


	
