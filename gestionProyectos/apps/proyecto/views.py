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

'''def asignar_proyecto(request):
    if request.method == 'POST':
        form = ProyectoUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        form = ProyectoUsuarioForm()
    return render(request, 'proyecto/asignar_proyecto.html',{'form': form})'''
