from django.db import models
from django.contrib.auth.models import User

 # Create your models here.

#user = User.objects.create_user(username='eliana',
#                              password='eliana123')


class login(models.Model):
    username = models.CharField(max_length=200)
    passsword = models.CharField(max_length=200)
    
    def __str__(self):
        return self.username+ "password"


class cpassword(models.Model):
    password  = models.CharField(max_length=10)
    newpassword = models.CharField(max_length=10)
    comfirmpassword = models.CharField(max_length=10)
    

    def __str__(self):
        return self.newpassword+"comfirmpassword"


class menu(models.Model):

    def __str__(self):
        return self.menu

    def __unicode__(self):
        return self.menu


class desbloqueo(models.Model):
    estado = models.CharField(max_length=20)
    
    def __str__(self):
        return self.desbloqueo

    def __unicode__(self):
        return self.desbloqueo

class bloquear_usuario(models.Model):
    
    def __str__(self):
        return self.user+ "userDetails"
    
    def __unicode__(self):
        return self.user

class desbloquear_usuario(models.Model):
    
    def __str__(self):
        return self.estado+ "userDetails"
    
    def __unicode__(self):
        return self.estado
      
class fechaexpi(models.Model):
    
    def __str__(self):
        return self.fechaexpi

    def __unicode__(self):
        return self.fechaexpi

class cambiarfecha(models.Model):
    fechactual = models.DateField(10)
    fechanueva = models.DateField(10)
    
    def __str__(self):
        return self.cambiarfecha



