from django.urls import re_path
from .views import listaDeUnidades, prueba

urlpatterns = [
    re_path(r'^$', listaDeUnidades),
    re_path(r'^imagenAatrox$', prueba),
]
