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
from apps.rol.views import registrar_rol, editar_rol, listar_rol, eliminar_rol
from apps.proyecto.views import registrar_proyecto, editar_proyecto, listar_proyecto, eliminar_proyecto, listar_tarea_proyecto
from apps.tarea.views import registrar_tarea, listar_tarea, editar_tarea, eliminar_tarea
from apps.linea_base.views import crear_linea_base, agregar_tareas,seleccion_linea_base,seleccion_tarea,actualizar_tarea

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
    # Proyectos
    path('registrar_proyecto/', registrar_proyecto),
    path('listar_proyecto/', listar_proyecto),
    path('editar_proyecto/<id_proyecto>/', editar_proyecto, name='editar_proyecto'),
    path('eliminar_proyecto/<id_proyecto>/', eliminar_proyecto, name='eliminar_proyecto'),
	path('listar_tarea_proyecto/<id_proyecto>/', listar_tarea_proyecto, name='listar_tarea_proyecto'),
    # Tareas
    path('registrar_tarea/<id_proyecto>/', registrar_tarea, name='registrar_tarea'),
    path('listar_tarea/<id_proyecto>', listar_tarea, name='listar_tarea'),
    path('editar_tarea/<id_tarea>/', editar_tarea, name='editar_tarea'),
    path('eliminar_tarea/<id_tarea>/', eliminar_tarea, name='eliminar_tarea'),
    #Linea Base
    path('crear_linea_base/',crear_linea_base),
    path('agregar_tareas/', agregar_tareas),
    path('seleccion_linea_base/<id_proyecto>',seleccion_linea_base,name='seleccion_linea_base'),
    path('seleccion_tarea/<lb>/<id_proyecto>', seleccion_tarea, name='seleccion_tarea'),
    path('actualizar_tarea/<id_tarea>/<lb>',actualizar_tarea, name='actualizar_tarea'),

    
    path('admin/', admin.site.urls),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
