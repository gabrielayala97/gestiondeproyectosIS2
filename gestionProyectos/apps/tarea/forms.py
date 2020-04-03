from django import forms
from apps.tarea.models import Tarea

class TareaForm (forms.ModelForm):
	class Meta:
		model = Tarea
		
		fields = [
			'version',
			'prioridad',
			'estado',
			'descripcion',
			'observacion',
			'id_tarea_padre',
		]
		
		labels = {
			'version': 'Version de la Tarea',
			'prioridad':'Prioridad',
			'estado': 'Estado',
			'descripcion':'Descripcion',
			'observacion': 'Observacion',
			'id_tarea_padre': 'ID de Tarea Padre',
		}
		
		widgets = {
			'version': forms.TextInput(attrs={'class':'form-control'}),
			'prioridad': forms.Select(attrs={'class':'form-control'}),
			'estado': forms.Select(attrs={'class':'form-control'}),
			'descripcion': forms.TextInput(attrs={'class':'form-control'}),
			'observacion': forms.TextInput(attrs={'class':'form-control'}),
			'id_tarea_padre': forms.TextInput(attrs={'class':'form-control'}),
		}