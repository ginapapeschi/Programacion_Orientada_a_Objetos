from claseVehiculo import Vehiculo

class Colectivo(Vehiculo):
    __nomEmpresa: str
    __capacidadCombustible: float
    __tipoCombustible: str

    def __init__(self, pat, cap, km, nom, capComb, tipo):
        super().__init__(pat, cap, km)
        self.__nomEmpresa = nom
        self.__capacidadCombustible = capComb
        self.__tipoCombustible = tipo

    def __str__(self):
        return f'''{super().__str__()}
Empresa: {self.__nomEmpresa}
Capacidad combustible: {self.__capacidadCombustible}
Combustible: {self.__tipoCombustible}'''

    def getNombre(self):
        return self.__nomEmpresa
    
    def getCapacidadCombustible(self):
        return self.__capacidadCombustible
    
    def getTipoCombustible(self):
        return self.__tipoCombustible
    
    def getPatente(self):
        return super().getPatente()
    
    def getCantidadPasajeros(self):
        return super().getCapacidad()
    
    def calcularConsumo(self):
        if self.__tipoCombustible.lower() == 'gasoil':
            consumo = super().getKmARecorrer() * 0.2
        elif self.__tipoCombustible.lower() == 'gnc':
            consumo = super().getKmARecorrer() * 0.15
        return consumo