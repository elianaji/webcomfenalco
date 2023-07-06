from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.forms import SelectDateWidget


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect(menu)
        
        else:
            messages.warning(request, 'Nombre de usuario y/o contraseña inconrrecta')
            
            return render(request, 'cpassword.html')


def cpassword(request):
    
    if request.method == 'POST':
        password = request.POST.get('password')
        newpassword = request.POST.get('newpassword')
        comfirmpassword = request.POST.get('comfirmpassword')

        authenticate_user = authenticate(request, username=request.user.username, newpassword=newpassword,)

        if password is not None:
            #Actualizar la contraseña
            authenticate_user.set_password(newpassword)
            authenticate_user.save()
            login(request, authenticate_user)
            return redirect('login')

        else:
            messages.warning (request, 'contraseña incorrecta, porfavor intente de nuevo')

    return render(request, 'cpassword.html' )

def menu(request):
    return render(request, 'menu.html')

def desbloqueo(request):
    if request.method == 'GET':
        return render(request, 'desbloqueo.html')
    
    elif request.method == 'POST':
        return JsonResponse('bloquear_usuario.html')
        user = authenticate(request, user= userDetails)
    
    else:
        return JsonResponse(request, 'desbloquear_usuario.html')
        

def bloquear_usuario(request, User):
    
    try:
        user = user.objects.get(id=username)
    except user.DoesNotExist:
        messages.error(request, 'El usuario no existe')
        return redirect('desbloqueo')
    
    if user.is_active:
        user.is_active = False
        user.save()
        messages.success(request, 'el usuario a sido bloqueado exitosamente')
        
    else:
        messages.info(request, 'usuario bloqueado')
        
    return redirect('userDetails')

def desbloquear_usuario(request, User):
    try:
        user = user.objects.get(id=username)
    except user.DoesNotExist:
        messages.error(request, 'El usuario no existe')
        return redirect('desbloqueo')
    
    if not user.is_active:
        user.is_active = True 
        user.save()
        messages.success(request, 'el usuario a sido desbloqueado exitosamente')
    else:
        messages.info(request, 'usuario desbloqueado')
        
    return redirect(userDetails)

def fechaexpi(request):
    return render(request, 'fechaexpi.html')

def cambiarfecha(request):
    return render (request, 'cambiarfecha.html')
    
