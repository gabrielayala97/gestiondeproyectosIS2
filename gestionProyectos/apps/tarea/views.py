from django.shortcuts import render, redirect

from .forms import TareaForm
from .models import Tarea

# Create your views here.
def registrar_tarea(request):
	if request.method == 'POST':
		form = TareaForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/')
	else:
		form = TareaForm()
	return render(request, 'tarea/tarea_form.html',{'form': form})

def listar_tarea(request):
	tarea = Tarea.objects.all().order_by('id')
	return render(request, 'tarea/listar_tarea.html',{'Tareas': tarea})
