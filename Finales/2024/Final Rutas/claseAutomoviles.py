from claseVehiculos import Vehiculo

class Automovil(Vehiculo):
    __maxPasajeros: int
    __cantRealTransportados: int

    def __init__(self, matr, model, costo, cant, maxP, cantReal):
        super().__init__(matr, model, costo, cant)
        self.__maxPasajeros = maxP
        self.__cantRealTransportados = cantReal

    def __str__(self):
        return f'''{super().__str__()}
Máximo de pasajeros: {self.__maxPasajeros}
Cantidad real transportados al momento del alquiler: {self.__cantRealTransportados}'''
    
    def getMaxPasajeros(self):
        return self.__maxPasajeros
    
    def getCantRealTransportados(self):
        return self.__cantRealTransportados
    
    # Inciso c
    def calcularAlquiler(self):
        return super().getCantDiasAlq() * super().getCosto() + 5000 * self.__cantRealTransportados
