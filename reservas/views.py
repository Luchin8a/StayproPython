from django.shortcuts import render
#importamos una clase para hacer el registro de usuarios
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib.auth.models import User


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
                return render(request, "register.html", {
              #cuando llamamos form en el documento html se crea un formuario
                  'form' : UserCreationForm,
                  'error' : 'Usuario registrado exitosamente'})
            except:
                return render(request, "register.html", {
            #cuando llamamos form en el documento html se crea un formuario
                  'form' : UserCreationForm,
                  'error' : "Usuario existente en la base de datos"})
        return render(request, "register.html", {
        #cuando llamamos form en el documento html se crea un formuario
                  'form' : UserCreationForm,
                  'error' : "Las contraseñas no coinciden"})  
    
