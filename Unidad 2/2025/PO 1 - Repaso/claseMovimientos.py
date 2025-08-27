class Movimiento:
    __numTarjeta: int
    __fecha: str
    __descripcion: str
    __tipoMovimiento: str
    __importe: float

    def __init__(self, numT, fecha, desc, tipoMov, imp):
        self.__numTarjeta = numT
        self.__fecha = fecha
        self.__descripcion = desc
        self.__tipoMovimiento = tipoMov
        self.__importe = imp

    def __str__(self):
        return f"{self.__fecha:<15} | {self.__descripcion:<25} | ${self.__importe:<11.2f} | {self.__tipoMovimiento:<5}"


    def __lt__(self, otro):
        return (self.__fecha, self.__tipoMovimiento) < (otro.getFecha(), otro.getTipoMov())

    def getNumTarjeta(self):
        return self.__numTarjeta

    def getFecha(self):
        return self.__fecha

    def getDescripcion(self):
        return self.__descripcion

    def getTipoMov(self):
        return self.__tipoMovimiento
            
    def getImporte(self):
        return self.__importe
    