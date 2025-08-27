from abc import ABC, abstractmethod

class Plan(ABC):
    __nomCompania: str
    __duracion: int
    __coberturaGeo: str
    __precioBase: float

    def __init__(self, nom, dur, cobertura, precio):
        self.__nomCompania = nom
        self.__duracion = dur
        self.__coberturaGeo = cobertura
        self.__precioBase = precio

    def __str__(self):
        return f'''Nombre de la compañía: {self.__nomCompania}
Duración del plan: {self.__duracion}
Cobertura geográfica: {self.__coberturaGeo}
Precio base: ${self.__precioBase}'''

    def getNomCompania(self):
        return self.__nomCompania
    
    def getDuracion(self):
        return self.__duracion
    
    def getCobertura(self):
        return self.__coberturaGeo
    
    def getPrecioBase(self):
        return self.__precioBase
    
    @abstractmethod
    def getImporteFinal(self):
        pass