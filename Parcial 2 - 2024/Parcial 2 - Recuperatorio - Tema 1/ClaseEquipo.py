import abc
from abc import ABC

class Equipo(ABC):
    __marca: str
    __modelo: str
    __anio: int
    __tipoCombustible: str
    __potencia: str 
    __capacidadCarga: int
    __tarifaAlquiler: int
    __cantDiasAlq: int

    def __init__ (self, marca, model, a, tipo, pot, cap, tarifa, cant):
        self.__marca = marca
        self.__modelo = model
        self.__anio = a
        self.__tipoCombustible = tipo
        self.__potencia = pot
        self.__capacidadCarga = cap
        self.__tarifaAlquiler = tarifa
        self.__cantDiasAlq = cant
        
    def getMarca(self):
        return self.__marca
    
    def getModelo(self):
        return self.__modelo
    
    def getAnio(self):
        return self.__anio
    
    def getTipoCombustible(self):
        return self.__tipoCombustible
    
    def getPotencia(self):
        return self.__potencia
    
    def getCapacidadCarga(self):
        return self.__capacidadCarga
    
    def getTarifaAlq(self):
        return self.__tarifaAlquiler
    
    def getCantDiasAlq(self):
        return self.__cantDiasAlq
    
    @abc.abstractmethod
    def calcularTarifaAlquiler(self):
        pass