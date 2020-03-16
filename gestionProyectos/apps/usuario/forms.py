from django import forms
from apps.usuario.models import Usuario

class UsuarioForm (forms.ModelForm):
	class Meta:
		model = Usuario
		
		fields = [
			'nombre', 
			'apellido',
			'email',
			'username',
			'password',
		]
		
		labels = {
			'nombre': 'Nombre', 
			'apellido':'Apellido',
			'email':'Correo Electronico',
			'username': 'Username',
			'password': 'Contraseña',
		}
		
		widgets = {
			'nombre': forms.TextInput(attrs={'class':'form-control'}), 
			'apellido': forms.TextInput(attrs={'class':'form-control'}),
			'email': forms.TextInput(attrs={'class':'form-control'}),
			'username': forms.TextInput(attrs={'class':'form-control'}),
			'password': forms.TextInput(attrs={'class':'form-control'}),
		}