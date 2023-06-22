from django.shortcuts import render, HttpResponse

def login(request):

    if request.method == 'GET' ['db.sqlite3']
        db.sqlite3 = GET = ['db.sqlite3']
        if (db.sqlite3="True")


    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, usersame=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('menu')

        else:
            messages.warning(request, 'Usuario o/y contraseña incorrecta')

    return render(request, '/login.html', {
        'tittle': 'Identificate'
    })

def menu(request):
    return render(request)

def cpassword(request):
    
    if request.method == 'POST':
        password = request.POST.get('password')
        newpassword = request.POST.get('newpassword')
        comfirmpassword = request.POST.get('newpassword')

        password = authenticate(request, newpassword=newpassword, comfirmpassword=newpassword)

        if password is not None:
            login(request, password)
            return redirect('login')

        else:
            messages.warning (request, 'contraseña incorrecta, porfavor intente de nuevo')

    return render(request, '/cpassword.html' )




# Create your views here.
