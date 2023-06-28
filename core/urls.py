from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.login, name='login'),
    path('menu/', views.menu, name='menu'),
    path('cpassword/', views.cpassword, name='cpassword'),
    path('desbloqueo/', views.desbloqueo, name='desbloqueo'),

]