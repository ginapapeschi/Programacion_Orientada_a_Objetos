class Movimiento:
    __numTarjeta: int
    __fecha: str
    __descripcion: str
    __tipoMovimiento: str
    __importe: float

    def __init__(self, numTarjeta, fecha, descripcion, tipoMovimiento, importe):
        self.__numTarjeta = numTarjeta
        self.__fecha = fecha
        self.__descripcion = descripcion
        self.__tipoMovimiento = tipoMovimiento
        self.__importe = importe

    def __lt__(self, otro):
        return self.__numTarjeta < otro.getNumTarjeta()

    def getNumTarjeta(self):
        return self.__numTarjeta
    
    def getFecha(self):
        return self.__fecha
    
    def getDescripcion(self):
        return self.__descripcion
    
    def getTipoMovimiento(self):
        return self.__tipoMovimiento
    
    def getImporte(self):
        return self.__importe   