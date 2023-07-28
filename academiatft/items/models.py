from django.db import models

class Componente(models.Model):
    nombre = models.CharField(max_length=50)


class Item(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=1000)
    componentes = models.ManyToManyField(Componente)
