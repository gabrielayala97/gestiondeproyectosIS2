"""gestionProyectos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from apps.usuario import views
from apps.rol.views import registrar_rol, editar_rol, listar_rol, eliminar_rol, asignar_rol
from apps.proyecto.views import registrar_proyecto, editar_proyecto, listar_proyecto, eliminar_proyecto
from apps.tarea.views import registrar_tarea, listar_tarea

urlpatterns = [
	path('', views.welcome),
    # Usuarios
	path('login/', views.login),
	path('logout/',views.logout),
	path('registrar_usuario/',views.crear_usuario),
    path('listar_usuarios/', views.listar_usuario),
    path('editar_usuario/<id_usuario>/', views.editar_usuario,name='editar_usuario'),
    path('eliminar_usuario/<id_usuario>/', views.eliminar_usuario,name='eliminar_usuario'),
    # Roles
	path('registrar_rol/', registrar_rol),
    path('listar_rol/', listar_rol),
    path('editar_rol/<id_rol>/', editar_rol, name='editar_rol'),
    path('eliminar_rol/<id_rol>/', eliminar_rol, name='eliminar_rol'),
    path('asignar_rol/', asignar_rol),
    # Proyectos
    path('registrar_proyecto/', registrar_proyecto),
    path('listar_proyecto/', listar_proyecto),
    path('editar_proyecto/<id_proyecto>/', editar_proyecto, name='editar_proyecto'),
    path('eliminar_proyecto/<id_proyecto>/', eliminar_proyecto, name='eliminar_proyecto'),
    # Tareas
    path('registrar_tarea/', registrar_tarea),
    path('listar_tarea/', listar_tarea),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
