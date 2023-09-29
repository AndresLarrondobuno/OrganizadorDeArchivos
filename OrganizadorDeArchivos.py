import os
import shutil
from Archivo import Archivo

class OrganizadorDeArchivos:
    def __init__(self, rutaAlDirectorio: str):
        self._directorio = rutaAlDirectorio 
        self._archivos: list[Archivo] = self.obtenerArchivos(rutaAlDirectorio)


    def obtenerArchivo(self, ruta: str) -> Archivo:
        for archivo in Archivo.__subclasses__():
            if hasattr(archivo, 'esExtensionValida') and callable(archivo.esExtensionValida):
                if archivo.esExtensionValida(ruta):
                    return archivo(ruta)


    def obtenerArchivos(self, rutaAlDirectorio: str):
        archivos = []
        elementosDelDirectorio = self.obtenerElementosDelDirectorio(rutaAlDirectorio)
        for elemento in elementosDelDirectorio:
            ruta = self.obtenerRuta(rutaAlDirectorio, elemento)
            if self.esUnArchivo(ruta):
                archivo = self.obtenerArchivo(ruta)
                archivos.append(archivo)
        return archivos
       

    def organizarArchivos(self):
        print(f'Organizando directorio {self._directorio}...')
        for archivo in self._archivos:
            rutaDestino = self.obtenerRuta(self._directorio, archivo._nombreDeDirectorioDestino)
            if not self.rutaExiste(rutaDestino):
                self.crearDirectorio(rutaDestino)
            self.moverArchivo(archivo._ruta, rutaDestino)



    def moverArchivo(self, rutaOrigen: str, rutaDestino: str):
        shutil.move(rutaOrigen, rutaDestino)


    def mostrarDirectorio(self, rutaAlDirectorio: str):
        print(f'\n Directorio ubicado en: {rutaAlDirectorio}')
        elementos = self.obtenerElementosDelDirectorio(rutaAlDirectorio)
        for elemento in elementos:
            ruta = self.obtenerRuta(rutaAlDirectorio, elemento)
            if self.esUnArchivo(ruta):
                print('  ' + elemento)
            if self.esUnDirectorio(ruta):
                print('  ' + elemento + ' [directorio]')
    

    def obtenerRuta(self, rutaAlDirectorio: str, nombreDeComponente: str) -> str:
        return os.path.join(rutaAlDirectorio, nombreDeComponente)
    

    def obtenerElementosDelDirectorio(self, rutaAlDirectorio: str)  -> list[str]:
        return os.listdir(rutaAlDirectorio)


    def esUnArchivo(self, ruta: str) -> bool:
        return os.path.isfile(ruta)
    

    def esUnDirectorio(self, ruta: str) -> bool:
        return os.path.isdir(ruta)


    def rutaExiste(self, ruta: str) -> bool:
        return os.path.exists(ruta)


    def contieneSubdirectorios(self, rutaAlDirectorio: str):
        elementos = self.obtenerElementosDelDirectorio(rutaAlDirectorio)
        for elemento in elementos:
            ruta = self.obtenerRuta(rutaAlDirectorio, elemento)
            if self.esUnDirectorio(ruta):
                return True


    def crearDirectorio(self, ruta: str):
        try:
            os.makedirs(ruta)
        except FileExistsError:
            print(f'El directorio {ruta} ya existe.')
        except OSError as e:
            print(f'Error al crear el directorio: {e}')