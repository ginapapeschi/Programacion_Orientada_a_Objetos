from clasePlanes import Plan

class Telefonia(Plan):
    __tipoLlamada: str
    __cantMinutos: int

    def __init__(self, nom, dur, cobertura, precio, tipoLlamada, cantMinutos):
        super().__init__(nom, dur, cobertura, precio)
        self.__tipoLlamada = tipoLlamada
        self.__cantMinutos = cantMinutos

    def __str__(self):
        return f'''{super().__str__()}
Tipo de llamada: {self.__tipoLlamada}
Cantidad de minutos: {self.__cantMinutos}'''
    
    def mostrarInfoSuper(self):
        return super().__str__()    

    def getTipo(self):
        return self.__tipoLlamada
    
    def getCantMinutos(self):
        return self.__cantMinutos
    
    def getImporteFinal(self):
        if self.__tipoLlamada == 'larga distancia':
            importe = super().getPrecioBase()

        elif self.__tipoLlamada == 'internacional':
            recargo = 20 * super().getPrecioBase() / 100
            importe = super().getPrecioBase() + recargo

        elif self.__tipoLlamada == 'locales':
            descuento = 7.5 * super().getPrecioBase() / 100
            importe = super().getPrecioBase() - descuento

        return importe
    
    def getNomCompania(self):
        return super().getNomCompania()
    
    def __lt__(self, otro):
        if self.__class__.__name__ != otro.__class__.__name__:
            # Comparación principal, ordena por nombre de clase.
            resultado = self.__class__.__name__ < otro.__class__.__name__
        
        else: 
            # Comparación secundaria, para ordenar por nombre de compañía.
            resultado = self.getNomCompania() < otro.getNomCompania()

        return resultado