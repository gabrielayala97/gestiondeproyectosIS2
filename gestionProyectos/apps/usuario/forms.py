from django import forms
from django.contrib.auth.forms import UserCreationForm
from apps.usuario.models import Usuario
#from django.contrib.auth.hashers import make_password
#UserCreationForm
#forms.ModelForm
class UsuarioForm (UserCreationForm):

	class Meta:
		model = Usuario

		fields = [
			'first_name', 
			'last_name',
			'email',
			'username',
			'password1',
			'password2',
			'rol',
		]
		
		labels = {
			'first_name': 'Nombre', 
			'last_name':'Apellido',
			'email':'Correo Electronico',
			'username': 'Username',
			'password1': 'Contraseña',
			'password2': 'Contraseña',
			'rol': 'Rol',
		}
		
		widgets = {
			'first_name': forms.TextInput(attrs={'class':'form-control'}), 
			'last_name': forms.TextInput(attrs={'class':'form-control'}),
			'email': forms.TextInput(attrs={'class':'form-control'}),
			'username': forms.TextInput(attrs={'class':'form-control'}),
			#'password': forms.TextInput(attrs={'class':'form-control'}),
			'password1' : forms.PasswordInput(),
			'password2' : forms.PasswordInput(),
			'rol': forms.Select(attrs={'class':'form-control'}),
		}
		
class UsuarioEditForm(forms.ModelForm):

	class Meta:
		model = Usuario

		fields = [
			'first_name', 
			'last_name',
			'email',
			'username',
			#'password1',
			#'password2',
			'rol',
		]
		
		labels = {
			'first_name': 'Nombre', 
			'last_name':'Apellido',
			'email':'Correo Electronico',
			'username': 'Username',
			#'password1': 'Contraseña',
			#'password2': 'Contraseña',
			'rol': 'Rol',
		}
		
		widgets = {
			'first_name': forms.TextInput(attrs={'class':'form-control'}), 
			'last_name': forms.TextInput(attrs={'class':'form-control'}),
			'email': forms.TextInput(attrs={'class':'form-control'}),
			'username': forms.TextInput(attrs={'class':'form-control'}),
			#'password': forms.TextInput(attrs={'class':'form-control'}),
			#'password1' : forms.PasswordInput(),
			#'password2' : forms.PasswordInput(),
			'rol': forms.Select(attrs={'class':'form-control'}),
		}


"""
		fields = [
			'first_name', 
			'last_name',
			'email',
			'username',
			'password',
			'rol',
		]
		
		labels = {
			'first_name': 'Nombre', 
			'last_name':'Apellido',
			'email':'Correo Electronico',
			'username': 'Username',
			'password': 'Contraseña',
			'rol': 'Rol',
		}
		
		widgets = {
			'first_name': forms.TextInput(attrs={'class':'form-control'}), 
			'last_name': forms.TextInput(attrs={'class':'form-control'}),
			'email': forms.TextInput(attrs={'class':'form-control'}),
			'username': forms.TextInput(attrs={'class':'form-control'}),
			'password': forms.TextInput(attrs={'class':'form-control'}),
			#'password1' : forms.PasswordInput(),
			#'password2' : forms.PasswordInput(),
			'rol': forms.Select(attrs={'class':'form-control'}),
		}
"""