class Paciente:
    __dni: str
    __nombre: str
    __unidad: str

    def __init__(self, dni, nom, uni):
        self.__dni = dni
        self.__nombre = nom
        self.__unidad = uni

    def __str__(self):
        return f"{self.__nombre}"
    
    def __lt__(self, otro):
        return (self.__unidad, self.__nombre) < (otro.getUnidad(), otro.getNombre())

    def getDNI(self):
        return self.__dni
    
    def getNombre(self):
        return self.__nombre
    
    def getUnidad(self):
        return self.__unidad