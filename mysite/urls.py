"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#aquí hacemos las importaciones de las vistas
from django.contrib import admin
from django.urls import path
from reservas import views

#aquí se establecen las urls
urlpatterns = [
    path('admin/', admin.site.urls),
    #el primer parametro es la url y el segundo desde que carpeta se llama
    path('home/', views.home, name="home"),
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    #la ruta de registro
    path('register/', views.registrar, name="registrar" ),
    path('reservas/', views.reservas, name="reservas" ),
    path('logout/', views.cerrarSesion, name='cerrarSesion'),
    path('iniciarSesion/', views.iniciarSesion, name='iniciarSesion'),
    path('login/', views.login, name="login")
]
