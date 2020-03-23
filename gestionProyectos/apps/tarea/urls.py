from django.urls import path
from apps.tarea import views

urlpatterns = [
	path('registrar_tarea/', views.registrar_tarea),
	path('listar_tarea/', views.listar_tarea),
	path('editar_tarea/<id_tarea>/', views.editar_tarea, name='editar_tarea'),
    path('eliminar_tarea/<id_tarea>/', views.eliminar_tarea, name='eliminar_tarea'),
]