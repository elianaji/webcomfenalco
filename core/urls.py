from django.urls import path
from . import views

urlpatterns = [

    path('login/', views.login),
    path('menu/', views.menu),
    path('cpassword/', views.cpassword),
    path('desbloqueo/', views.desbloqueo),

]