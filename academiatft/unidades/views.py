from django.shortcuts import render
from .models import Unidad, Habilidad

def run():
    print('unidades.models corrio correctamente!')


def listaDeUnidades(request):
    unidades = Unidad.objects.all()
    return render(request, 'listaDeUnidades.html', {'unidades':unidades})


def prueba(request):
    
    return render(request, 'renderizarImagenTest.html')