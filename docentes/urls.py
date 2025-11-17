from django.urls import path
from .views import docentes_view

urlpatterns = [
    path("", docentes_view, name="docentes"),
]