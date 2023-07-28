from django.shortcuts import render
from django.db import models

def inicio(request):
    return render(request, 'inicio.html')

