import pandas as pd
import json, ast
import sys
sys.path.append(r'c:\\Programacion\\python\\mvc tft\\academiatft')
from academiatft.administradorDeRutasDeArchivos import obtenerRutaAArchivo


def evaluar(expresion: str):
    try:
        ast.literal_eval(expresion)
    except ValueError:
        print(f'expresion: {expresion}')
        return

    return expresion


def deserializarCamposString(dataframe: pd.DataFrame):

    def evaluacionSeguraDeLiteral(val):
        try:
            return ast.literal_eval(val)
        except (ValueError):
            return val
        
    columnaStatsTransformadaADict = dataframe['stats'].apply(evaluacionSeguraDeLiteral)
    columnaHabilidadTransformadaADict = dataframe['ability'].apply(evaluacionSeguraDeLiteral)
    columnaRasgosTransformadaALista = dataframe['traits'].apply(evaluacionSeguraDeLiteral)
    dataframe['stats'] = columnaStatsTransformadaADict
    dataframe['ability'] = columnaHabilidadTransformadaADict
    dataframe['traits'] = columnaRasgosTransformadaALista

    return dataframe


def castearColumnaStatsAFloat(dataframe: pd.DataFrame):
    for i, fila in dataframe.iterrows():
        fila['stats']['mana'] = float(fila['stats']['mana'])
        fila['stats']['initialMana'] = float(fila['stats']['initialMana'])
    return dataframe


def validarCampo(campo):
    if isinstance(campo, (list, dict)):
        return bool(campo)  #verificar en caso de lista o diccionario si no estan vacios
    elif pd.isna(campo) or campo == '':
        return False
    return True


def eliminarDatosNulos(df: pd.DataFrame): 
    mascara = df.applymap(validarCampo).all(axis=1)
    dfSinDatosNulos = df[mascara]
    return dfSinDatosNulos


def construirDataframeUnidades():
    rutaLocalDeDataDragonJson = obtenerRutaAArchivo('dataDragon.json')

    with open(rutaLocalDeDataDragonJson) as tftDataJson:

        data = json.load(tftDataJson)

        dataUnidadesSet9 = data["setData"][2]["champions"]

        dataframe = pd.DataFrame(dataUnidadesSet9)

        dataframe = dataframe.loc[dataframe['characterName'].str.contains('TFT9', na=False)]

        labelsReordenadosParaColumnas = ['name', 'traits', 'cost', 'ability', 'stats']

        dataframe = dataframe.reindex(columns=labelsReordenadosParaColumnas)

        dataframe = castearColumnaStatsAFloat(dataframe)

        dataframe = deserializarCamposString(dataframe)

        dataframe = eliminarDatosNulos(dataframe)

        return dataframe
    
pd.set_option('display.max_colwidth', 1500)

df = construirDataframeUnidades()

#ryze = df.loc[df['name'] == 'Ryze']
#print(ryze['stats'].iloc[6]['mana'])

print(df)