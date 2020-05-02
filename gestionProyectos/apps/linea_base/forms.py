from django import forms
from apps.linea_base.models import LineaBase

class LineaBaseForm (forms.ModelForm):
	class Meta:
		model = LineaBase

		fields = [
			'linea_base',
            'estado',
		]
		
		labels = {
			'linea_base': 'Descripcion',
            'estado':'Estado',
		}
		
		widgets = {
			'linea_base': forms.TextInput(attrs={'class':'form-control'}),
            'estado': forms.Select(attrs={'class':'form-control'}),
		}