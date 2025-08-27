class Atencion:
    __dniAtencion: str
    __fecha: str
    __importe: float

    def __init__(self, dni, fecha, imp):
        self.__dniAtencion = dni
        self.__fecha = fecha
        self.__importe = imp

    def getDNIAtencion(self):
        return self.__dniAtencion
    
    def getFecha(self):
        return self.__fecha
    
    def getImporte(self):
        return self.__importe
    