from django.shortcuts import render, redirect

from .forms import TareaForm, Editar_tarea_Form
from .models import Tarea
from django.contrib.auth.decorators import login_required

from apps.proyecto.models import Proyecto 
from apps.usuario.models import Usuario

# Create your views here.
@login_required(login_url='/login')
def registrar_tarea(request,id_proyecto):
	proyecto = Proyecto.objects.get(id=id_proyecto)
	if request.method == 'POST':
		form = TareaForm(proyecto,request.POST)
		if form.is_valid():
			form.save()
		return redirect('/')
	else:
		form = TareaForm(proyecto)
	return render(request, 'tarea/tarea_form.html',{'form': form})

@login_required(login_url='/login')
def listar_tarea(request,id_proyecto):
	tarea = Tarea.objects.filter(proyecto = id_proyecto)
	return render(request, 'tarea/listar_tarea.html',{'Tareas': tarea})
		
@login_required(login_url='/login')	
def editar_tarea(request, id_tarea):
	# Recuperamos la instancia de la tarea
	instancia = Tarea.objects.get(id=id_tarea)

	if request.method == "GET":
		# Actualizamos el formulario con los datos recibidos
		form = Editar_tarea_Form(instance=instancia)
	else:
		form = Editar_tarea_Form(request.POST,instance=instancia)
		if form.is_valid():
			form.save()
		return redirect('listar_tarea', id_proyecto=instancia.proyecto.id)
	return render(request, 'tarea/tarea_form.html',{'form': form})

@login_required(login_url='/login')
def eliminar_tarea(request,id_tarea):
    tarea = Tarea.objects.get(id = id_tarea)
    auxiliar = tarea.proyecto.id
    tarea.delete()
    return redirect('listar_tarea', id_proyecto=auxiliar)





