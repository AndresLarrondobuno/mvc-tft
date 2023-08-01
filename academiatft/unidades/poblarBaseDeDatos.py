import pandas as pd
from .models import Unidad, Habilidad, Rasgo

def run():
    print('unidades.poblarBaseDeDatos corrio correctamente!')


def insertarUnidad(filaUnidad: pd.Series):
    nombreHabilidad = filaUnidad['ability']['name']
    descripcionHabilidad = filaUnidad['ability']['desc']
    habilidad = Habilidad(nombre=nombreHabilidad, descripcion=descripcionHabilidad)
    habilidad.save()

    rasgos = filaUnidad['traits']
    rasgos = [Rasgo(nombre=nombreDeRasgo) for nombreDeRasgo in rasgos]
    for rasgo in rasgos:
        rasgo.save()

    nombre = filaUnidad['name']
    coste = filaUnidad['cost']
    vida = filaUnidad['stats']['hp']
    armadura = filaUnidad['stats']['armor']
    resistenciaMagica = filaUnidad['stats']['magicResist']
    dano = filaUnidad['stats']['damage']
    velocidadDeAtaque = filaUnidad['stats']['attackSpeed']
    chanceDeCritico = filaUnidad['stats']['critChance']
    multiplicadorDeCritico = filaUnidad['stats']['critMultiplier']
    manaInicial = filaUnidad['stats']['initialMana']
    mana = filaUnidad['stats']['mana']
    rango = filaUnidad['stats']['range']


    unidad = Unidad(nombre=nombre,
                    coste=coste,
                    habilidad=habilidad,
                    vida=vida,
                    armadura=armadura,
                    resistenciaMagica=resistenciaMagica,
                    dano=dano,
                    velocidadDeAtaque=velocidadDeAtaque,
                    chanceDeCritico=chanceDeCritico,
                    multiplicadorDeCritico=multiplicadorDeCritico,
                    manaInicial=manaInicial,
                    mana=mana,
                    rango=rango)

    unidad.save()
    idsRasgos = [rasgo.id for rasgo in rasgos]
    unidad.rasgos.set(idsRasgos)


def insertarUnidades(dataframe: pd.DataFrame):
    for i,fila in dataframe.iterrows():
        insertarUnidad(fila)



