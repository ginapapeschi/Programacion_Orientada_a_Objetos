from abc import abstractmethod

class Vehiculo:
    __matricula: str
    __modelo: str
    __costoKM: float
    __cantDiasAlq: int

    def __init__(self, matr, model, costo, cant):
        self.__matricula = matr
        self.__modelo = model
        self.__costoKM = costo
        self.__cantDiasAlq = cant

    def __str__(self):
        return f'''Matricula: {self.__matricula}
Modelo: {self.__modelo}
Costo por kilómetro: ${self.__costoKM:.2f}
Cantidad de días de alquiler: {self.__cantDiasAlq}'''

    def getMatricula(self):
        return self.__matricula
    
    def getModelo(self):
        return self.__modelo
    
    def getCosto(self):
        return self.__costoKM
    
    def getCantDiasAlq(self):
        return self.__cantDiasAlq
    
    # Inciso c
    @abstractmethod
    def calcularAlquiler(self):
        pass