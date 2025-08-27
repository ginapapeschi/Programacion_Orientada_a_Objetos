class Cliente:
    __nombre: str
    __apellido: str
    __dniCliente: int
    __numTarjeta: int
    __saldoAnterior: float

    def __init__(self, nombre, apellido, dniCliente, numTarjeta, saldoAnterior):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__dniCliente = dniCliente
        self.__numTarjeta = numTarjeta
        self.__saldoAnterior = saldoAnterior

    def getNombre(self):
        return self.__nombre
    
    def getApellido(self):
        return self.__apellido
    
    def getDNICliente(self):
        return self.__dniCliente
    
    def getNumTarjeta(self):
        return self.__numTarjeta
    
    def getSaldoAnterior(self):
        return self.__saldoAnterior
    
    def setSaldo(self, saldoActual):
        self.__saldoAnterior = saldoActual