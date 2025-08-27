from claseVehiculos import Vehiculo

class Camion(Vehiculo):
    __capacidadMax: float
    __cantRealTransportada: float
    __rutas: list

    def __init__(self, matr, model, costo, cant, capMax, cantTransp):
        super().__init__(matr, model, costo, cant)
        self.__capacidadMax = capMax
        self.__cantRealTransportada = cantTransp
        self.__rutas = []

    def __str__(self):
        return f'''{super().__str__()}
Capacidad máxima de carga: {self.getCapacidadMax}
Cantidad real transportada al momento del alquiler: {self.__cantRealTransportada}'''

    def getCapacidadMax(self):
        return self.__capacidadMax
    
    def getCantRealTransportada(self):
        return self.__cantRealTransportada
    
    def agregarRuta(self, unaRuta):
        self.__rutas.append(unaRuta)
    
    # Inciso a
    def tieneRuta(self):
        if len(self.__rutas) is 0:
            tiene = False
        else:
            tiene = True

        return tiene

    # Inciso b
    def mostrarRutas(self):
        print()
        print(f"---- RUTAS ASIGNADAS ----".center(40))
        print()
        for ruta in self.__rutas:
            print()
            print(ruta)

    # Inciso c
    def calcularAlquiler(self):
        if self.__cantRealTransportada > 4500:
            alquiler = (super().getCantDiasAlq() * super().getCosto()) + (super().getCosto() * 0.05)
        
        elif self.__cantRealTransportada <= 4500:
            alquiler = (super().getCantDiasAlq() * super().getCosto()) + (super().getCosto() * 0.02)

        return alquiler