from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages

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
            
            return render(request, 'login.html')


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
    opcion = request.GET('opcion')
    
    if opcion == 'submit1':
        return redirect('cpassword.html')
    
    elif opcion == 'submit2':
        return redirect('desbloqueo.html')
    
    elif opcion == 'submit3':
        return redirect('fechaexpi.html')



def desbloqueo(request):
    return render(request, 'desbloqueo.html')

def fechaexpi(request):
    return render(request, 'desbloqueo.html')