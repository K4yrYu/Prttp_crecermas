from django.shortcuts import render

def estudiantes_view(request):
    return render(request, "estudiantes.html")
