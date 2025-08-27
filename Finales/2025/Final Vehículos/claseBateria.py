class Bateria:
    __patente: str
    __marca = "CATL"
    __capacidadCarga: float
    __cargaActual: float

    def __init__(self, pat, cap, carga):
        self.__patente = pat
        self.__capacidadCarga = cap
        self.__cargaActual = carga

    def __str__(self):
        return f'''Patente: {self.__patente}
Marca: {self.__marca}
Capacidad: {self.__capacidadCarga}
Carga actual: {self.__cargaActual}'''

    def getPatente(self):
        return self.__patente
    
    def getCapacidadCarga(self):
        return self.__capacidadCarga
    
    def getCargaActual(self):
        return self.__cargaActual
    
    @classmethod
    def getMarca(cls):
        return cls.__marca
    
    def calcularEnergiaDisponible(self):
         return(self.__capacidadCarga - self.__cargaActual) / 10
    