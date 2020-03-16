from django.urls import path
from apps.rol import views

urlpatterns = [
	path('registrar_rol/', views.registrar_rol),
	path('listar_rol/', views.listar_rol), 
	path('editar_rol/<id_rol>/', views.editar_rol, name='editar_rol')
	path('eliminar_rol/<id_rol>/', views.eliminar_rol, name='eliminar_rol'),   
	path('asignar_rol/', views.asignar_rol),                             
]