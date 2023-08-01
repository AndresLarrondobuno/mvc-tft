import pandas as pd
import json
import sys
sys.path.append(r'c:\\Programacion\\python\\mvc tft\\academiatft')

from academiatft.procesadorDeDatos import ProcesadorDeDatos
from academiatft.administradorDeRutasDeArchivos import AdministradorDeRutasDeArchivos


class LimpiadorDeDatos:
    def construirDataframeUnidades():
        rutaLocalDeDataDragonJson = AdministradorDeRutasDeArchivos.obtenerRutaAArchivo('dataDragon.json')

        with open(rutaLocalDeDataDragonJson) as tftDataJson:

            data = json.load(tftDataJson)

            dataUnidadesSet9 = data["setData"][2]["champions"]

            dataframe = pd.DataFrame(dataUnidadesSet9)

            dataframe = dataframe.loc[dataframe['characterName'].str.contains('TFT9', na=False)]

            labelsReordenadosParaColumnas = ['name', 'traits', 'cost', 'ability', 'stats']

            dataframe = dataframe.reindex(columns=labelsReordenadosParaColumnas)

            dataframe = ProcesadorDeDatos.castearColumnaStatsAFloat(dataframe)

            dataframe = ProcesadorDeDatos.deserializarCamposString(dataframe)

            dataframe = ProcesadorDeDatos.eliminarDatosNulos(dataframe)

            return dataframe
    
pd.set_option('display.max_colwidth', 1000)

df = LimpiadorDeDatos.construirDataframeUnidades()

#ryze = df.loc[df['name'] == 'Ryze']
#print(ryze['stats'].iloc[6]['mana'])

print(df)