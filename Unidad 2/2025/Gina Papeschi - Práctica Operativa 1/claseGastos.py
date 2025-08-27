# Nombre: Papeschi Gina
# DNI: 46407532
# Número de registro: E010-252

class Gasto:
    __patente: str
    __fecha: str
    __importe: float
    __descripcion: str

    def __init__(self, pat, fecha, imp, desc):
        self.__patente = pat
        self.__fecha = fecha
        self.__importe = imp
        self.__descripcion = desc

    def __lt__(self, otro):
        resultado = None
        if self.__fecha == otro.getFecha():
            resultado = self.__patente < otro.getPatente().lower()
        else:
            resultado = self.__fecha < otro.getFecha()

        return resultado

    def getPatente(self):
        return self.__patente
    
    def getFecha(self):
        return self.__fecha
    
    def getImporte(self):
        return self.__importe
    
    def getDescripcion(self):
        return self.__descripcion