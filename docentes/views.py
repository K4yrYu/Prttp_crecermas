from django.shortcuts import render

def docentes_view(request):
    return render(request, "docentes.html")