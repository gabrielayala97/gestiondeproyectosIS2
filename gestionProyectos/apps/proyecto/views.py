from django.shortcuts import render, redirect

from .forms import ProyectoForm
from .models import Proyecto
from django.contrib.auth.decorators import login_required
#from apps.rol.forms_asignar_rol import UsuarioRolForm

from apps.tarea.models import Tarea

# Create your views here.
@login_required(login_url='/login')
def registrar_proyecto(request):
	if request.method == 'POST':
		form = ProyectoForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/')
	else:
		form = ProyectoForm()
	return render(request, 'proyecto/proyecto_form.html',{'form': form})

@login_required(login_url='/login')
def listar_proyecto(request):
	if request.user.is_superuser :
		proyecto = Proyecto.objects.all().order_by('id')
		return render(request, 'proyecto/listar_proyecto.html',{'Proyectos': proyecto})
	else:
		proyecto = Proyecto.objects.filter(usuarios = request.user.id)
		return render(request, 'proyecto/listar_proyecto.html',{'Proyectos': proyecto})
		
@login_required(login_url='/login')
def listar_tarea_proyecto(request, id_proyecto):
	tarea = Tarea.objects.filter(proyecto = id_proyecto)
	return render(request, 'tarea/listar_tarea.html',{'Tareas': tarea})

@login_required(login_url='/login')
def editar_proyecto(request, id_proyecto):
    # Recuperamos la instancia del proyecto
    instancia = Proyecto.objects.get(id=id_proyecto)

    if request.method == "GET":
        # Actualizamos el formulario con los datos recibidos
        form = ProyectoForm(instance=instancia)
    else:
        form = ProyectoForm(request.POST,instance=instancia)
        if form.is_valid():
            form.save()
        return redirect('/listar_proyecto')
    return render(request, 'proyecto/proyecto_form.html',{'form': form})

@login_required(login_url='/login')
def eliminar_proyecto(request,id_proyecto):
    proyecto = Proyecto.objects.get(id = id_proyecto)
    proyecto.delete()
    return redirect('/listar_proyecto')

'''def asignar_proyecto(request):
    if request.method == 'POST':
        form = ProyectoUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        form = ProyectoUsuarioForm()
    return render(request, 'proyecto/asignar_proyecto.html',{'form': form})'''
