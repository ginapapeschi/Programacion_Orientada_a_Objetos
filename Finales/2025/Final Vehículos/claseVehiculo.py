import abc
from abc import abstractmethod

class Vehiculo(abc.ABC):
    __patente: str
    __capacidadPasajeros: int
    __kmARecorrer: float

    def __init__(self, pat, cap, km):
        self.__patente = pat
        self.__capacidadPasajeros = cap
        self.__kmARecorrer = km

    def __str__(self):
        return f'''Patente: {self.__patente}
Capacidad: {self.__capacidadPasajeros}
KM a recorrer: {self.__kmARecorrer}'''

    def getPatente(self):
        return self.__patente
    
    def getCapacidad(self):
        return self.__capacidadPasajeros
    
    def getKmARecorrer(self):
        return self.__kmARecorrer

    @abstractmethod
    def calcularConsumo(self):
        pass