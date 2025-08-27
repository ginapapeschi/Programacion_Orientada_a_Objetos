# Nombre: Papeschi Gina
# DNI: 46407532
# Número de registro: E010-252

class Movilidad:
    __patente: str
    __tipo: str
    __capacidadCarga: int
    __importeMensual: float
    __marca: str
    __modelo: str

    def __init__(self, pat, tipo, capacidad, imp, marca, modelo):
        self.__patente = pat
        self.__tipo = tipo
        self.__capacidadCarga = capacidad
        self.__importeMensual = imp
        self.__marca = marca
        self.__modelo = modelo

    def getPatente(self):
        return self.__patente
    
    def getTipo(self):
        return self.__tipo
    
    def getCapacidadCarga(self):
        return self.__capacidadCarga
    
    def getImporteMensual(self):
        return self.__importeMensual
    
    def getMarca(self):
        return self.__marca
    
    def getModelo(self):
        return self.__modelo