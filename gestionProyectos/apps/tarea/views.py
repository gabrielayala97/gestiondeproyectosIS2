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
	
def editar_tarea(request, id_tarea):
	# Recuperamos la instancia de la tarea
	instancia = Tarea.objects.get(id=id_tarea)

	if request.method == "GET":
		# Actualizamos el formulario con los datos recibidos
		form = TareaForm(instance=instancia)
	else:
		form = TareaForm(request.POST,instance=instancia)
		if form.is_valid():
			form.save()
		return redirect('/listar_tarea')
	return render(request, 'tarea/tarea_form.html',{'form': form})

def eliminar_tarea(request,id_tarea):
    tarea = Tarea.objects.get(id = id_tarea)
    tarea.delete()
    return redirect('/listar_tarea')
