from django import forms
from .models import Usuario

class UsuarioForm (forms.ModelForm):
	class Meta:
		model = Usuario
		
		fields = [
			'nombre', 
			'apellido',
			'email',
			'password',
		]
		
		labels = {
			'nombre': 'Nombre', 
			'apellido':'Apellido',
			'email':'Correo Electronico',
			'password': 'Contraseña',
		}
		
		widgets = {
			'nombre': forms.TextInput(attrs={'class':'form-control'}), 
			'apellido': forms.TextInput(attrs={'class':'form-control'}),
			'email': forms.TextInput(attrs={'class':'form-control'}),
			'password': forms.TextInput(attrs={'class':'form-control'}),
		}