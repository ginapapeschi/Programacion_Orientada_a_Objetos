class Cliente:
    __nombre: str
    __apellido: str
    __dni: str
    __numTarjeta: int
    __saldoAnterior: float

    def __init__(self, nom, ap, dni, numT, sald):
        self.__nombre = nom
        self.__apellido = ap
        self.__dni = dni
        self.__numTarjeta = numT
        self.__saldoAnterior = sald

    def getNombre(self):
        return self.__nombre
    
    def getApellido(self):
        return self.__apellido
    
    def getDNI(self):
        return self.__dni
    
    def getNumTarjeta(self):
        return self.__numTarjeta
    
    def getSaldoAnterior(self):
        return self.__saldoAnterior