class Nacimiento:
    __dniMama: int
    __tipoParto: str
    __fecha: str
    __hora: str
    __peso: float
    __altura: float

    def __init__(self, dni, tipo, fecha, hora, peso, alt):
        self.__dniMama = dni
        self.__tipoParto = tipo
        self.__fecha = fecha
        self.__hora = hora
        self.__peso = peso
        self.__altura = alt
    
    def __eq__(self, otro):
        return self.__dniMama == otro.getDNIMama() and self.__fecha == otro.getFecha()

    def getDNIMama(self):
        return self.__dniMama
    
    def getTipoParto(self):
        return self.__tipoParto
    
    def getFecha(self):
        return self.__fecha
    
    def getHora(self):
        return self.__hora
    
    def getPeso(self):
        return self.__peso
    
    def getAltura(self):
        return self.__altura