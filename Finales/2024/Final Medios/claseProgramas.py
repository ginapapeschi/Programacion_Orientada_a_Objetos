import datetime

class Programa:
    __nombre: str
    __horaInicio: datetime
    __horaFin: datetime

    def __init__(self, nom, horaI, horaF):
        self.__nombre = nom
        self.__horaInicio = horaI
        self.__horaFin = horaF

    def __str__(self):
        return f'''{self.__nombre} | {self.__horaInicio.strftime("%H:%M")} - {self.__horaFin.strftime("%H:%M")}'''

    def getNombre(self):
        return self.__nombre
    
    def getHoraInicio(self):
        return self.__horaInicio
    
    def getHoraFin(self):
        return self.__horaFin