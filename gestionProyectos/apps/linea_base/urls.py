from django.urls import path
from apps.linea_base import views

urlpatterns = [
    path('crear_linea_base/',views.crear_linea_base),
    path('agregar_tareas/', views.agregar_tareas),
    path('seleccion_linea_base/<id_proyecto>',views.seleccion_linea_base,name='seleccion_linea_base'),
    path('seleccion_tarea/<lb>/<id_proyecto>', views.seleccion_tarea, name='seleccion_tarea'),
    path('actualizar_tarea/<id_tarea>/<lb>',views.actualizar_tarea, name='actualizar_tarea'),
]