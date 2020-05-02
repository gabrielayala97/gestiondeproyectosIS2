from django import forms
from apps.tarea.models import Tarea
from apps.proyecto.models import Proyecto

class TareaForm (forms.ModelForm):
	
	def __init__(self, proyecto, *args, **kwargs):
		super(TareaForm, self).__init__(*args, **kwargs)
		auxiliar=list()
		tareas = Tarea.objects.filter(proyecto = proyecto.id)
		longitud = len(tareas)
		if longitud > 0:
			for t in tareas:
				auxiliar.append(t.id)
			id_auxiliar = auxiliar[-1]
			self.fields['proyecto'].queryset =Proyecto.objects.filter(id = proyecto.id)
			self.fields['id_tarea_padre'].queryset =Tarea.objects.filter(id = id_auxiliar)
		else:
			self.fields['proyecto'].queryset =Proyecto.objects.filter(id = proyecto.id)
			self.fields['id_tarea_padre'].queryset =Tarea.objects.filter(id = None)
	class Meta:
		model = Tarea
		fields = [
			'version',
			'prioridad',
			'estado',
			'descripcion',
			'observacion',
			'proyecto',
			'id_tarea_padre',
		]
		
		labels = {
			'version': 'Version de la Tarea',
			'prioridad':'Prioridad',
			'estado': 'Estado',
			'descripcion':'Descripcion',
			'observacion': 'Observacion',
			'proyecto': 'Proyecto',
			'id_tarea_padre': 'ID de Tarea Padre',
		}
		
		widgets = {
			'version': forms.TextInput(attrs={'class':'form-control'}),
			'prioridad': forms.Select(attrs={'class':'form-control'}),
			'estado': forms.Select(attrs={'class':'form-control'}),
			'descripcion': forms.TextInput(attrs={'class':'form-control'}),
			'observacion': forms.TextInput(attrs={'class':'form-control'}),
		}
class Editar_tarea_Form(forms.ModelForm):

	class Meta:
		model = Tarea
		fields = [
			'version',
			'prioridad',
			'estado',
			'descripcion',
			'observacion',
		]
		
		labels = {
			'version': 'Version de la Tarea',
			'prioridad':'Prioridad',
			'estado': 'Estado',
			'descripcion':'Descripcion',
			'observacion': 'Observacion',
		}
		
		widgets = {
			'version': forms.TextInput(attrs={'class':'form-control'}),
			'prioridad': forms.Select(attrs={'class':'form-control'}),
			'estado': forms.Select(attrs={'class':'form-control'}),
			'descripcion': forms.TextInput(attrs={'class':'form-control'}),
			'observacion': forms.TextInput(attrs={'class':'form-control'}),
		}