import abc
from abc import ABC

class Publicacion:                          # SUPERCLASE de la que se va a heredar en las subclases.
    __titulo: str
    __categoria: str
    __precio_base: float

    def __init__ (self, tit, cat, precio):
        self.__titulo = tit
        self.__categoria = cat
        self.__precio_base = precio

    def getTitulo(self):
        return self.__titulo
    
    def getCategoria(self):
        return self.__categoria
    
    def getPrecioBase(self):
        return self.__precio_base
    
    @abc.abstractmethod
    def getImporteVenta(self):
        pass
