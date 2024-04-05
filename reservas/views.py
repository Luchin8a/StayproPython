from django.shortcuts import render
from django.http import HttpResponse

# Crear las vistas aquí.
def hello(request):
    return HttpResponse("Hola Bogotá!")
