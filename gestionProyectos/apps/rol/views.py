from django.shortcuts import render, redirect

from .forms_rol import RolForm
from .models import Rol
#from apps.rol.forms_asignar_rol import UsuarioRolForm

# Create your views here.
def registrar_rol(request):
	if request.method == 'POST':
		form = RolForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/')
	else:
		form = RolForm()
	return render(request, 'rol/rol_form.html',{'form': form})

def listar_rol(request):
	rol = Rol.objects.all().order_by('id')
	return render(request, 'rol/listar.html',{'Roles': rol})
	
def editar_rol(request, id_rol):
    # Recuperamos la instancia del rol
    instancia = Rol.objects.get(id=id_rol)

    if request.method == "GET":
        # Actualizamos el formulario con los datos recibidos
        form = RolForm(instance=instancia)
    else:
        form = RolForm(request.POST,instance=instancia)
        if form.is_valid():
            form.save()
        return redirect('/listar_rol')
    return render(request, 'rol/rol_form.html',{'form': form})

def eliminar_rol(request,id_rol):
    rol = Rol.objects.get(id = id_rol)
    rol.delete()
    return redirect('/listar_rol')

"""def asignar_rol(request):
    if request.method == 'POST':
        form = UsuarioRolForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        form = UsuarioRolForm()
    return render(request, 'rol/asignar_rol.html',{'form': form})"""


