from django.shortcuts import render, redirect
#importamos una clase para hacer el registro de usuarios y autenticación
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse
from django.contrib.auth.models import User
#importamos el metodo login que crea una cookie
from django.contrib.auth import login, logout, authenticate
#importamos una excepcion para errores en la base de datos
from django.db import IntegrityError



# Crear las vistas aquí.
def home(request):
    return render(request, "home.html")

def registrar(request):

    if request.method == 'GET':
        return render(request, "register.html", {
        #cuando llamamos form en el documento html se crea un formuario
                  'form' : UserCreationForm
                  })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'],
                password=request.POST['password1'])
                user.save()
                #para que login guarde el usuario en la cookie, haciendo una sesión
                login(request, user)
                #redirect para redirigirlo a reservas
                return redirect('reservas')
            #usamos la excepción con el error en  la base de datos           
            except IntegrityError:
                return render(request, "register.html", {
            #cuando llamamos form en el documento html se crea un formuario
                  'form' : UserCreationForm,
                  'error' : "Usuario existente en la base de datos"})
        return render(request, "register.html", {
        #cuando llamamos form en el documento html se crea un formuario
                  'form' : UserCreationForm,
                  'error' : "Las contraseñas no coinciden"})  

def reservas(request):
    return render(request, 'reservas_habitacion.html')

def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def login(request):
    return render(request, 'dashboard\login.html')
    
def cerrarSesion(request):
    logout(request)
    return redirect('home')

def iniciarSesion(request):
    if request.method == 'GET':
        return render(request, 'iniciarSesion.html',{
            'form' : AuthenticationForm,
        })
    else:
        user = authenticate(request, username=request.POST['username'],
                     password=request.POST['password'] )
        if user is None:
             return render(request, 'iniciarSesion.html',{
            'form' : AuthenticationForm,
            'error' : "El usuario o la contraseña son incorrectas"
            })
        else:
            login(request, user)
            return redirect('reservas')
      