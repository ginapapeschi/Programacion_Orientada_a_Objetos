from clasePlanes import Plan

class Television(Plan):
    __cantCanalesNacionales: int
    __cantCanalesInternacionales: int

    def __init__(self, nom, dur, cobertura, precio, cantNac, cantInter):
        super().__init__(nom, dur, cobertura, precio)
        self.__cantCanalesNacionales = cantNac
        self.__cantCanalesInternacionales = cantInter

    def __str__(self):
        return f'''{super().__str__()}
Cantidad de canales nacionales: {self.__cantCanalesNacionales}
Cantidad de canales internacionales: {self.__cantCanalesInternacionales}'''

    def mostrarInfoSuper(self):
        return super().__str__()

    def getCantCanalesNacionales(self):
        return self.__cantCanalesNacionales
    
    def getCantCanalesInternacionales(self):
        return self.__cantCanalesInternacionales
    
    # Inciso 3
    def getImporteFinal(self):
        if self.__cantCanalesInternacionales > 10:
            recargo = 15 * super().getPrecioBase() / 100
            importe = super().getPrecioBase() + recargo

        else:
            importe = super().getPrecioBase()

        return importe
    
    # Inciso 3 y 4
    def getNomCompania(self):
        return super().getNomCompania()
    
    # Inciso 4
    def __lt__(self, otro):
        if self.__class__.__name__ != otro.__class__.__name__:
            # Comparación principal, ordena por nombre de clase.
            resultado = self.__class__.__name__ < otro.__class__.__name__
        
        else: 
            # Comparación secundaria, para ordenar por nombre de compañía.
            resultado = self.getNomCompania() < otro.getNomCompania()

        return resultado