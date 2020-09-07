from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from apps.usuario import views

urlpatterns = [
	path('welcome', views.welcome),
	path('register', views.register),
	path('login/',views.login),
	path('logout/',views.logout),
	path('registrar_usuario/',views.crear_usuario),
	path('listar_usuarios/', views.listar_usuario),
	path('mostrar_perfil/<id_usuario>', views.listar_usuario, name='mostrar_perfil'),
    path('editar_usuario/<id_usuario>/', views.editar_usuario, name='editar_usuario'),
    path('eliminar_usuario/<id_usuario>/', views.eliminar_usuario, name='eliminar_usuario'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)