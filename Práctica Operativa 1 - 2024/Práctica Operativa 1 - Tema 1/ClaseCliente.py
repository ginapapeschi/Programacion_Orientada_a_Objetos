class Cliente:
    __nombre: str
    __apellido: str
    __dni: int
    __nro_tarjeta: int
    __saldo_anterior: float

    def __init__(self, nom, ap, xdni, nro_t, sald_ant):
        self.__nombre = nom
        self.__apellido = ap
        self.__dni = xdni
        self.__nro_tarjeta = nro_t
        self.__saldo_anterior = sald_ant
    
    def getNombre(self):
        return self.__nombre
    
    def getApellido(self):
        return self.__apellido
    
    def getDNI(self):
        return self.__dni
    
    def getNro_tarjeta(self):
        return self.__nro_tarjeta
    
    def getSaldo_anterior(self):
        return self.__saldo_anterior