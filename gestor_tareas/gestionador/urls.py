from django.urls import path
from . import views

urlpatterns = [
    path('tareas/', views.obtener_tareas, name='obtener_tareas'),
    path('tareas/agregar/', views.agregar_tarea, name='agregar_tarea'),
    path('tareas/actualizar/<int:identificador_tarea>/', views.actualizar_tarea, name='actualizar_tarea'),
    path('tareas/eliminar/<int:identificador_tarea>/', views.eliminar_tarea, name='eliminar_tarea'),
]
