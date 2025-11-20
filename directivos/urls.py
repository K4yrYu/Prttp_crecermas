from django.urls import path
from .views import directivos_view

urlpatterns = [
    path("", directivos_view, name="directivos"),
]