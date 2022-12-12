from django.urls import path
from .views import prueba, prueba_render, Familiar

urlpatterns = [
    path("prueba/", prueba, name="prueba"),
    path("prueba_render/", prueba_render, name="prueba_render"),
    path("familiar/", Familiar, name="Familiar"),

]