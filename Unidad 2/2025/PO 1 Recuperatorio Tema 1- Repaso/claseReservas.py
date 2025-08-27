class Reserva:
    __numReserva: int
    __nomPersona: str
    __numCabañaAsignada: int
    __fechaInicio: str
    __cantHuespedes: int
    __cantDias: int
    __importeSeña: float

    def __init__(self, numR, nom, numC, fecha, cantH, cantD, imp):
        self.__numReserva = numR
        self.__nomPersona = nom
        self.__numCabañaAsignada = numC
        self.__fechaInicio = fecha
        self.__cantHuespedes = cantH
        self.__cantDias = cantD
        self.__importeSeña = imp

    def getNumReserva(self):
        return self.__numReserva
    
    def getNomPersona(self):
        return self.__nomPersona
    
    def getNumCabaña(self):
        return self.__numCabañaAsignada
    
    def getFecha(self):
        return self.__fechaInicio
    
    def getCantHuespedes(self):
        return self.__cantHuespedes
    
    def getCantDias(self):
        return self.__cantDias
    
    def getImporte(self):
        return self.__importeSeña