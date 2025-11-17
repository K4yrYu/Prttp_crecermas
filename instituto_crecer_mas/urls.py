from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

urlpatterns = [
    path('admin/', admin.site.urls),

    # Rutas de las apps
    path('docentes/', include('docentes.urls')),
    path('estudiantes/', include('estudiantes.urls')),

    # tus otras páginas
    path('', lambda request: render(request, 'home.html'), name='home'),
    path('login/', lambda request: render(request, 'login.html'), name='login'),
    path('signup/', lambda request: render(request, 'signup.html'), name='signup'),
]
