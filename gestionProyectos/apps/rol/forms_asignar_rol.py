from django import forms
from apps.usuario.models import Usuario 
from apps.rol.models import Rol


class UsuarioRolForm (forms.ModelForm):
	class Meta:
		model = Usuario
		
		fields = [
			#'nombre',
			'rol',
		]
		
		labels = {
			#'nombre': 'Usuario.nombre',
			'rol':'Rol.nombre_rol',
		}
		
		widgets = {
			#'usuario': forms.Select(),
			'rol': forms.Select(attrs={'class':'form-control'}), 
			#forms.CheckboxSelectMultiple(attrs={'class':'form-control'}),
		}