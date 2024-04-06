from django.shortcuts import render
#importamos una clase para hacer el registro de usuarios
from django.contrib.auth.forms import UserCreationForm


# Crear las vistas aquí.
def home(request):
    return render(request, "home.html")

def registrar(request):
    return render(request, "register.html", {
        #cuando llamamos form en el documento html se crea un formuario
                  'form' : UserCreationForm
                  })
