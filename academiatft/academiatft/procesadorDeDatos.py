import ast
import pandas as pd

# armar clase ProcesadorDeDatos, su responsabilidad va a ser facilitar el procesamiento de datos 
# parsing, formateo, casteo de tipos de datos

def deserializarCamposString(dataframe: pd.DataFrame):
    try:
        columnaStatsTransformadaADict = dataframe['stats'].apply(ast.literal_eval)
        columnaHabilidadTransformadaADict = dataframe['ability'].apply(ast.literal_eval)
        columnaRasgosTransformadaALista = dataframe['traits'].apply(ast.literal_eval)
        dataframe['stats'] = columnaStatsTransformadaADict
        dataframe['ability'] = columnaHabilidadTransformadaADict
        dataframe['traits'] = columnaRasgosTransformadaALista

    except Exception as excepcion:

        for idx, row in dataframe.iterrows():
            try:
                ast.literal_eval(row['stats'])
                ast.literal_eval(row['ability'])
                ast.literal_eval(row['traits'])
            except Exception as sub_e:
                print(f"Fila {idx}: {sub_e}")

    return dataframe


def castearColumnaStatsAFloat(dataframe: pd.DataFrame):
    for i, fila in dataframe.iterrows():
        fila['stats']['mana'] = float(fila['stats']['mana'])
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