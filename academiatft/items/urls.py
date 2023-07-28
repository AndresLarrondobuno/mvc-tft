from django.urls import re_path
from .views import listaDeItems, prueba

urlpatterns = [
    re_path(r'^$', listaDeItems),
    re_path(r'^imagenDeathblade$', prueba),
]
