import pandas as pd
import os, json, ast
from .models import Unidad, Habilidad, Rasgo


def run():
    print('unidades.poblarBaseDeDatos corrio correctamente!')


def construirCsvLimpio():
    rutaLocalDeDataDragonJson = obtenerRutaAArchivo('dataDragon.json')
    rutaLocalUnidadesSet9 = obtenerRutaAArchivo('unidadesSet9.csv')

    with open(rutaLocalDeDataDragonJson) as tftDataJson:

        data = json.load(tftDataJson)

        dataUnidadesSet9 = data["setData"][2]["champions"]

        dataframeUnidades = pd.DataFrame(dataUnidadesSet9)

        dataframeUnidadesSet9 = dataframeUnidades.loc[dataframeUnidades['characterName'].str.contains('TFT9', na=False)]

        labelsReordenadosParaColumnas = ['name', 'traits', 'cost', 'ability', 'stats']
        dataframeUnidadesSet9 = dataframeUnidadesSet9.reindex(columns=labelsReordenadosParaColumnas)

        dataframeUnidadesSet9.to_csv(rutaLocalUnidadesSet9, index=False)


def obtenerRutaAArchivo(nombreDelArchivo: str) -> str:
    return os.path.join(os.path.dirname(__file__), nombreDelArchivo)


def leerCsv(nombreArchivoCsv: str):
    ruta = obtenerRutaAArchivo(nombreArchivoCsv)
    dataframe = pd.read_csv(ruta)
    return dataframe


def transformarCamposString(dataframe: pd.DataFrame):
    columnaStatsTransformadaADict = dataframe['stats'].apply(ast.literal_eval)
    columnaHabilidadTransformadaADict = dataframe['ability'].apply(ast.literal_eval)
    columnaRasgosTransformadaALista = dataframe['traits'].apply(ast.literal_eval)
    dataframe['stats'] = columnaStatsTransformadaADict
    dataframe['ability'] = columnaHabilidadTransformadaADict
    dataframe['traits'] = columnaRasgosTransformadaALista

    return dataframe


def validarCampo(campo):
    if isinstance(campo, (list, dict)):
        return bool(campo)  #verificar en caso de lista o diccionario si no estan vacios
    elif pd.isna(campo) or campo == '':
        return False
    return True


def limpiarDatosNulos(df: pd.DataFrame): 
    mascara = df.applymap(validarCampo).all(axis=1)
    dfSinDatosNulos = df[mascara]
    return dfSinDatosNulos


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


def insertarUnidades():
    dataframe = getDataframe()

    for i,fila in dataframe.iterrows():
        insertarUnidad(fila)


def getDataframe(limpio: bool = True):
    dataframe = leerCsv('unidadesSet9.csv')
    if limpio:
        dataframe = transformarCamposString(dataframe)
        dataframe = limpiarDatosNulos(dataframe)
    return dataframe


pd.set_option('display.max_colwidth', 1500)

df = getDataframe(limpio=True)

dfMaokai = df.loc[df['name'] == 'Maokai'].iloc[0]

'''
print(dfMaokai['ability']['desc'])
print()
print(dfMaokai['ability']['variables'])
print()
'''

print(dfMaokai)
