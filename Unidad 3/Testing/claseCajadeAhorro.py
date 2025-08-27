class CajaDeAhorro:
    __numero: int
    __saldo: float
    __cbu: str
    __pesosExtraidos: float
    __apellido: str
    __nombre: str
    __cuil: str
    __maxExtraccionDiaria = 10000

    def __init__(self, num, sald, cbu, pesos, ap, nom, cuil):
        self.__numero = num
        self.__saldo = sald
        self.__cbu = cbu
        self.__pesosExtraidos = pesos
        self.__apellido = ap
        self.__nombre = nom
        self.__cuil = cuil

    def getSaldo(self):
        return self.__saldo
    
    def extraer(self, importe):
        self.__saldo -= importe
        self.__pesosExtraidos += importe

    def depositar(self, importe):
        self.__saldo += importe
    
    @classmethod
    def getMaximoExtraccionDiaria(cls):
        return cls.__maxExtraccionDiaria