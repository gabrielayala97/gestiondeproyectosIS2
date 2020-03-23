from django.urls import path
import views

urlpatterns = [
	path('registrar_proyecto/', views.registrar_proyecto),
	path('listar_proyecto/', views.listar_proyecto),
    path('editar_proyecto/<id_proyecto>/', views.editar_proyecto, name='editar_proyecto'),
    path('eliminar_proyecto/<id_proyecto>/', views.eliminar_proyecto, name='eliminar_proyecto'),
]
