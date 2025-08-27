from claseMedio import Medio

class Prensa(Medio):
    __tipoPublicacion: str
    __periodicidad: str

    def __init__(self, nom, aud, tipo, per):
        super().__init__(nom, aud)
        self.__tipoPublicacion = tipo
        self.__periodicidad = per

    def getTipo(self):
        return self.__tipoPublicacion
    
    def getPeriodicidad(self):
        return self.__periodicidad
    