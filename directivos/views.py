from django.shortcuts import render

def directivos_view(request):
    return render(request, "directivos.html")
