from django.shortcuts import render, HttpResponse


def login_view(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, usersame=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/menu')

        else:
            messages.warning(request, 'Usuario o/y contraseña incorrecta')

    return render(request, 'login.html', {
        'tittle': 'Ingresar'
    })


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
    opcion = request.POST.get('opcion')
    
    if opcion =='button':
            return redirect('cpassword.html')
        
    elif opcion =='button2':
            return redirect('fechaexpi.html')
        
    elif opcion =='button3':
            return redirect('desbloqueo.html')


def desbloqueo(request):

        if request.method == 'POST':
            username = request.POST.get('username')

        user = authenticate(request, usersame=username)

        if user is not None:
            login(request, user)
            return redirect('desbloqueo')

        else:
            messages.warning(request, 'porfavor verifique el username')


# Create your views here.
