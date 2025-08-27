class Programa:
    __nombre: str
    __horarioInicio: str
    __horarioFin: str

    def __init__(self, nom, inicio, fin):
        self.__nombre = nom
        self.__horarioInicio = inicio
        self.__horarioFin = fin

    def __str__(self):
        return f"Nombre: {self.__nombre} - Horario de inicio: {self.__horarioInicio} - Horario de fin: {self.__horarioFin}"

    def getNombre(self):
        return self.__nombre
    
    def getHorarioInicio(self):
        return self.__horarioInicio
    
    def getHorarioFin(self):
        return self.__horarioFin
    