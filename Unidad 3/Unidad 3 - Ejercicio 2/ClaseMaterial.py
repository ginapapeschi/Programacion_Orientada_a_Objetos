class Material:
    __material: int
    __caract: str
    __cantUti: float
    __costoAd: float

    def __init__ (self, mat, carac, cant, costo):
        self.__material = mat
        self.__caract = carac
        self.__cantUti = cant
        self.__costoAd = costo

    def getMaterial(self):
        return self.__material
    
    def getCaract(self):
        return self.__caract
    
    def getCantUti(self):
        return self.__cantUti
    
    def getCostoAdicional(self):
        return self.__costoAd