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
	
@login_required(login_url='/login')
def seleccion_linea_base(request, id_proyecto):
	tareas = Tarea.objects.all()
	lb = LineaBase.objects.all()
	auxiliar=list()
	lineasbase=list()
	proyecto = Proyecto.objects.get(id = id_proyecto)
	#Almacena los id de las lineas base que pertenecen a otros proyectos
	for t in tareas:
		if (t.linea_base is not None and t.proyecto != proyecto):
			auxiliar.append(t.linea_base.id)
	cantidad = len(auxiliar)
	if cantidad > 0:
		#Elimina los duplicados
		lista_nueva = list()
		for i in auxiliar:
			if i not in lista_nueva:
				lista_nueva.append(i)
		#agrega las lineas bases que no corresponden a otros proyectos
		for l in lb:
			if l.id not in lista_nueva:
					lineasbase.append(l)
		return render(request, 'linea_base/seleccion_linea_base.html',{'LBs': lineasbase,'id_proyecto':id_proyecto})
	else:
		return render(request, 'linea_base/seleccion_linea_base.html',{'LBs': lb,'id_proyecto':id_proyecto})

@login_required(login_url='/login')
def seleccion_tarea(request,lb,id_proyecto):
	tarea = Tarea.objects.filter(proyecto = id_proyecto)
	auxiliar=list()
	for t in tarea:
		if t.linea_base is None:
			auxiliar.append(t)
	if len(auxiliar) > 0:
		return render(request, 'linea_base/seleccion_tarea.html',{'Tareas': auxiliar,'LB':lb})
	else:
		messages.error(request, 'Las tareas del proyecto ya se encuentran dentro de una LB!')
		return render(request, 'linea_base/seleccion_tarea.html')
		
@login_required(login_url='/login')
def actualizar_tarea(request, id_tarea,lb):
	linea_base = LineaBase.objects.get(linea_base = lb)
	tarea = Tarea.objects.get(id = id_tarea)
	tarea.linea_base = linea_base
	tarea.save()
	return redirect('/seleccion_tarea/'+str(lb)+'/'+str(tarea.proyecto.id))

