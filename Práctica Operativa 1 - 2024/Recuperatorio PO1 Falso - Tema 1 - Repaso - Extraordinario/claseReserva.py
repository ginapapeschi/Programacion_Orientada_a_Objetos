class Reserva:
    __numReserva: int
    __nombre: str
    __numCabanaAsignada: int
    __fechaInicio: str
    __cantHuespedes: int
    __cantDias: int
    __importeSena: float

    def __init__(self, numR, nom, numC, fecha, cantH, cantD, imp):
        self.__numReserva = numR
        self.__nombre = nom
        self.__numCabanaAsignada = numC
        self.__fechaInicio = fecha
        self.__cantHuespedes = cantH
        self.__cantDias = cantD
        self.__importeSena = imp

    def getNumReserva(self):
        return self.__numReserva
    
    def getNombreReservo(self):
        return self.__nombre
    
    def getNumCabanaAsignada(self):
        return self.__numCabanaAsignada
    
    def getFechaInicio(self):
        return self.__fechaInicio
    
    def getCantHuespedes(self):
        return self.__cantHuespedes
    
    def getCantDias(self):
        return self.__cantDias
    
    def getImporteSena(self):
        return self.__importeSena