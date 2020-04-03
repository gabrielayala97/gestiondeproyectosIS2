
from django.urls import path
from apps.usuario import views

urlpatterns = [
	path('', views.welcome),
	#path('register', views.register),
	path('login/',views.login),
	path('logout/',views.logout),
	path('registrar_usuario/',views.crear_usuario),
	path('listar_usuarios/', views.listar_usuario),
    path('editar_usuario/<id_usuario>/', views.editar_usuario, name='editar_usuario'),
    path('eliminar_usuario/<id_usuario>/', views.eliminar_usuario, name='eliminar_usuario'),
]