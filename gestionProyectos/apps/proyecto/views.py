from django.shortcuts import render, redirect

from .forms import ProyectoForm
from .models import Proyecto
#from apps.rol.forms_asignar_rol import UsuarioRolForm

# Create your views here.
def registrar_proyecto(request):
	if request.method == 'POST':
		form = ProyectoForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/')
	else:
		form = ProyectoForm()
	return render(request, 'proyecto/proyecto_form.html',{'form': form})

def listar_proyecto(request):
	proyecto = Proyecto.objects.all().order_by('id')
	return render(request, 'proyecto/listar_proyecto.html',{'Proyectos': proyecto})

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
