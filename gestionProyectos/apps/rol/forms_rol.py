from django import forms
from apps.rol.models import Rol



class RolForm (forms.ModelForm):
	class Meta:
		model = Rol
		#CHOISES = ['Administracion', 'Desarrollo', 'Configuracion']
		
		fields = [
			'nombre_rol',
			#'permiso',
		]
		
		labels = {
			'nombre_rol': 'Nombre del Rol',
			#'permiso': 'Nombre del permiso',
		}
		
		widgets = {
			'nombre_rol': forms.TextInput(attrs={'class':'form-control'}),
			#'permiso': forms.Select(choise=CHOISES),
		}