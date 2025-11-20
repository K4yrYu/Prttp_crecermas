from django.shortcuts import render

def administrador_view(request):
    return render(request, "admin.html")

def usuarios_view(request):
    return render(request, "usuarios.html")

def matriculas_view(request):
    return render(request, "matriculas.html")

