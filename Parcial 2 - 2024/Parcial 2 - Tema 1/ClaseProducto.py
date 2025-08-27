import abc
from abc import ABC

class Producto:
    __nombre: str
    __fechaEnv: str
    __fechaVenc: str
    __temperatura: float 
    __paisOrigen: str
    __numLote: int
    __costo: float

    def __init__ (self, nom, fechaE, fechaV, temp, pais, num, costo):
        self.__nombre = nom
        self.__fechaEnv = fechaE
        self.__fechaVenc = fechaV
        self.__temperatura = temp
        self.__paisOrigen = pais
        self.__numLote = num
        self.__costo = costo

    def getNombre(self):
        return self.__nombre
    
    def getFechaEnv(self):
        return self.__fechaEnv
    
    def getFechaVenc(self):
        return self.__fechaVenc
    
    def getTemperatura(self):
        return self.__temperatura

    def getPais(self):
        return self.__paisOrigen
    
    def getNumLote(self):
        return self.__numLote
    
    def getCosto(self):
        return self.__costo
    
    @abc.abstractmethod
    def importeVenta(self):
        pass