from django.urls import path
from .views import estudiantes_view

urlpatterns = [
    path("", estudiantes_view, name="estudiantes"),
]