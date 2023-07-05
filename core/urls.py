from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.login, name='login'),
    path('menu/', views.menu, name='menu'),
    path('cpassword/', views.cpassword, name='cpassword'),
    path('desbloqueo/', views.desbloqueo, name='desbloqueo'),
    path('bloquear_usuario/', views.bloquear_usuario, name='bloquear_usuario'),
    path('desbloquear_usuario', views.desbloquear_usuario, name='desbloquear_usuario'),
    path('fechaexpi/', views.fechaexpi, name='fechaexpi'),
    path('cambiarfecha/', views.cambiarfecha, name='cambiarfecha'),

]