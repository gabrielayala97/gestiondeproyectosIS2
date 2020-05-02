from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import LineaBaseForm
from .models import LineaBase
from apps.proyecto.models import Proyecto
from apps.tarea.models import Tarea
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def crear_linea_base(request):
	if request.method == 'POST':
		form = LineaBaseForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/')
	else:
		form = LineaBaseForm()
	return render(request, 'linea_base/linea_base_form.html',{'form': form})

@login_required(login_url='/login')
def agregar_tareas(request):
    if request.user.is_superuser :
        proyecto = Proyecto.objects.all().order_by('id')
        return render(request, 'linea_base/seleccion_proyecto.html',{'Proyectos': proyecto})
    else:
        proyecto = Proyecto.objects.filter(usuarios = request.user.id)
        return render(request, 'linea_base/seleccion_proyecto.html',{'Proyectos': proyecto})
