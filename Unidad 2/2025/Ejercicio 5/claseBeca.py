class Beca:
    __idBeca: int
    __tipoBeca: str
    __importe: float

    def __init__(self, id, tipo, imp):
        self.__idBeca = id
        self.__tipoBeca = tipo
        self.__importe = imp

    def getIDBeca(self):
        return self.__idBeca
    
    def getTipoBeca(self):
        return self.__tipoBeca
    
    def getImporte(self):
        return self.__importe