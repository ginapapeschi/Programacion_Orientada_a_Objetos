from claseMedios import Medio

class PrensaEscrita(Medio):
    __periodicidad: str
    __cantSecciones: int

    def __init__(self, nom, aud, per, cantS):
        super().__init__(nom, aud)
        self.__periodicidad = per
        self.__cantSecciones = cantS

    def __str__(self):
        return f"{super().__str__()} - Periodicidad: {self.__periodicidad} - Cantidad de secciones: {self.__cantSecciones}"

    def getPeriodicidad(self):
        return self.__periodicidad
    
    def getCantSecciones(self):
        return self.__cantSecciones
    
    def getIndiceAudiencia(self):
        if self.__periodicidad.lower() == 'mensual':
            indice = super().getAudiencia() / self.__cantSecciones

        elif self.__periodicidad.lower() == 'semanal':
            indice = super().getAudiencia() / ((self.__cantSecciones) * 4)

        return indice