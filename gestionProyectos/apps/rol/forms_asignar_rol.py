from django import forms
from apps.rol.models import Usuario_Posee_Rol


class UsuarioRolForm (forms.ModelForm):
	class Meta:
		model = Usuario_Posee_Rol
		
		fields = [
			'usuario',
			'rol',
		]
		
		labels = {
			'usuario': 'Usuario',
			'rol':'Rol',
		}
		
		widgets = {
			'usuario': forms.Select(),
			'rol': forms.Select(attrs={'class':'form-control'}), 
			#forms.CheckboxSelectMultiple(attrs={'class':'form-control'}),
		}