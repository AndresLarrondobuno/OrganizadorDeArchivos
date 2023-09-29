from abc import ABC, abstractmethod
import os

class Archivo(ABC):
    EXTENSIONES_DE_TEXTO = ['.txt', '.rtf', '.docx']
    EXTENSIONES_DE_IMAGEN = ['.png', '.jpg', '.pdf']
    EXTENSIONES_DE_AUDIO = ['.wav', '.mp3', '.ogg']
    EXTENSIONES_DE_VIDEO = ['.mp4', '.avi', '.flv', '.wmv']
    EXTENCIONES_DE_EJECUTABLES = ['.exe']
    EXTENCIONES_DE_SCRIPT = ['.py', '.php', '.cpp']


    def __init__(self, ruta: str):
        self._ruta = ruta
        self._extension = Archivo.obtenerExtension(self._ruta)
        self._directorioPadre = self.obtenerDirectorioPadre()
        self._nombre = self.obtenerNombre()


    def __repr__(self) -> str:
        return self._ruta


    @abstractmethod
    def esExtensionValida(ruta):
        return


    @staticmethod
    def obtenerExtension(ruta: str) -> str:
        ultimoComponenteDeRuta = os.path.basename(ruta)
        nombre, extension = os.path.splitext(ultimoComponenteDeRuta)
        return extension


    def obtenerDirectorioPadre(self) -> str:
        return os.path.dirname(self._ruta)
    

    def obtenerNombre(self):
        return os.path.basename(self._ruta)
    

    def nuevaRuta(self) -> str:
        return


class ArchivoDeTexto(Archivo):
    def __init__(self, ruta: str):
        super().__init__(ruta)
        self._nombreDeDirectorioDestino = 'ArchivosDeTexto'
    

    def esExtensionValida(ruta):
        return True if Archivo.obtenerExtension(ruta) in Archivo.EXTENSIONES_DE_TEXTO else False
    

    def nuevaRuta(self) -> str:
        return os.path.join(self._directorioPadre, self._nuevoDirectorio ,self._nombre)


class ArchivoDeAudio(Archivo):
    def __init__(self, ruta: str):
        super().__init__(ruta)
        self._nombreDeDirectorioDestino = 'ArchivosDeAudio'
    

    def esExtensionValida(ruta):
        return True if Archivo.obtenerExtension(ruta) in Archivo.EXTENSIONES_DE_AUDIO else False
    

    def nuevaRuta(self):
        return


class ArchivoDeVideo(Archivo):
    def __init__(self, ruta: str):
        super().__init__(ruta)
        self._nombreDeNuevoDirectorio = 'ArchivosDeVideo'
    

    def esExtensionValida(ruta):
        return True if Archivo.obtenerExtension(ruta) in Archivo.EXTENSIONES_DE_VIDEO else False


class ArchivoDeImagen(Archivo):
    def __init__(self, ruta: str):
        super().__init__(ruta)
        self._nombreDeDirectorioDestino = 'ArchivosDeImagen'
    

    def esExtensionValida(ruta):
        return True if Archivo.obtenerExtension(ruta) in Archivo.EXTENSIONES_DE_IMAGEN else False


class ArchivoEjecutable(Archivo):
    def __init__(self, ruta: str):
        super().__init__(ruta)
        self._nombreDeDirectorioDestino = 'ArchivosEjecutables'

    def esExtensionValida(ruta):
        return True if Archivo.obtenerExtension(ruta) in Archivo.EXTENCIONES_DE_EJECUTABLES else False


class ArchivoDeScript(Archivo):
    def __init__(self, ruta: str):
        super().__init__(ruta)
        self._nombreDeDirectorioDestino = 'Scripts'
    

    def esExtensionValida(ruta):
        return True if Archivo.obtenerExtension(ruta) in Archivo.EXTENCIONES_DE_SCRIPT else False