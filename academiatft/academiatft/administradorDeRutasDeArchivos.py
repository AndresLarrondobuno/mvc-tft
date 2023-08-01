import os

def obtenerRutaAArchivo(nombreDeArchivo: str, rutaActual=None) -> str:
    if rutaActual is None:
        rutaActual = os.path.abspath(__file__)
        print(f"el archivo se encuentra en el directorio actual: {rutaActual}")

    rutaArchivoBuscado = os.path.join(rutaActual, nombreDeArchivo)

    if os.path.exists(rutaArchivoBuscado):
        print(f"el archivo fue encontrado en la ruta: {rutaArchivoBuscado}")
        return rutaArchivoBuscado

    directorioPadre = os.path.dirname(rutaActual)
    
    if directorioPadre == rutaActual:
        return None

    return obtenerRutaAArchivo(nombreDeArchivo, directorioPadre)