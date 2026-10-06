from django.urls import path
from . import views


urlpatterns = [
    path('', views.lista_citas, name='lista_citas'),
    path('registro/', views.registro, name='registro'),
    path('login/', views.iniciar_sesion, name='login'),
    path('logout/', views.cerrar_sesion, name='logout'),
    path('nueva/', views.crear_cita, name='crear_cita'),
    path('editar/<int:cita_id>/', views.editar_cita, name='editar_cita'),
    path('eliminar/<int:cita_id>/', views.eliminar_cita, name='eliminar_cita'),
]
