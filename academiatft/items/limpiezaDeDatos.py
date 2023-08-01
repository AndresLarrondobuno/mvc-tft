import pandas as pd
import os, json
from academiatft.academiatft.administradorDeRutasDeArchivos import AdministradorDeRutasDeArchivos
from academiatft.academiatft.procesadorDeDatos import ProcesadorDeDatos

def run():
    print('items.poblarBaseDeDatos corrio correctamente!')

nombresDeItems = [
    "Rabadon's Deathcap",
    "Archangel's Staff",
    "Locket of the Iron Solari",
    "Ionic Spark",
    "Morellonomicon",
    "Jeweled Gauntlet",
    "Blue Buff",
    "Protector's Vow",
    "Chalice of Power",
    "Redemption",
    "Hand Of Justice",
    "Bramble Vest",
    "Gargoyle Stoneplate",
    "Sunfire Cape",
    "Shroud of Stillness",
    "Dragon's Claw",
    "Zephyr",
    "Quicksilver",
    "Warmog's Armor",
    "Guardbreaker",
    "Tactician's Crown",
    "Edge of Night",
    "Thief's Gloves",
    "Shurima Emblem",
    "Sorcerer Emblem",
    "Challenger Emblem",
    "Ionia Emblem",
    "Juggernaut Emblem",
    "Slayer Emblem",
    "Noxus Emblem",
    "Demacia Emblem"]


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