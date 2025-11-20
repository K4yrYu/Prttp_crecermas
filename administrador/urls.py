from django.urls import path
from .views import administrador_view, usuarios_view, matriculas_view

urlpatterns = [
    path("", administrador_view, name="administrador"),
    path("usuarios/", usuarios_view, name="usuarios"),
    path("matriculas/", matriculas_view, name="matriculas"),
]
