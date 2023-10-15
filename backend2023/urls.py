"""
URL configuration for backend2023 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from firstApp import views


urlpatterns = [
    path('importaciones/agregarimpform', views.CrearImportacionForm),
    path('importaciones/',views.ImportacionData),
    path('importaciones/crearimp',views.CrearImportacion),
    path('importaciones/<id>',views.eliminarImportacion),
    path('importaciones/modificarImportacion/<id>',views.modificarImportacion),
    path('actualizar',views.actualizarImportacion)
]
