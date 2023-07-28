from django.db import models

def run():
    print('unidades.models corrio correctamente!')

class Habilidad(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()


class Rasgo(models.Model):
    nombre = models.CharField(max_length=50)



class Unidad(models.Model):
    nombre = models.CharField(max_length=50)
    rasgos = models.ManyToManyField(Rasgo)
    coste = models.IntegerField(default=0)
    habilidad = models.OneToOneField(Habilidad, on_delete=models.CASCADE)

    vida = models.IntegerField(default=0)
    armadura = models.IntegerField(default=0)
    resistenciaMagica = models.IntegerField(default=0)
    dano = models.IntegerField(default=0)
    velocidadDeAtaque = models.FloatField(default=0)
    chanceDeCritico = models.FloatField(default=0)
    multiplicadorDeCritico = models.FloatField(default=0)
    manaInicial = models.IntegerField(default=0)
    mana = models.IntegerField(default=0)
    rango = models.IntegerField(default=0)
    


