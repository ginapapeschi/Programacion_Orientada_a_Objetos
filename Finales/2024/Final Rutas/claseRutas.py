class Ruta:
    __codigo: int
    __destino: str
    __distanciaTotal: float
    __rutaAsignada: bool

    def __init__(self, cod, dest, dist, asignado):
        self.__codigo = cod
        self.__destino = dest
        self.__distanciaTotal = dist
        self.__rutaAsignada = asignado

    def __str__(self):
        return f'''Código: {self.__codigo}
Destino: {self.__destino}
Distancia total en kilómetros: {self.__distanciaTotal:.2f}'''
    
    def getCodigo(self):
        return self.__codigo
    
    def getDestino(self):
        return self.__destino
    
    def getDistanciaTotal(self):
        return self.__distanciaTotal
    
    def getRutaAsignada(self):
        return self.__rutaAsignada
    
    def setRutaAsignada(self, valor):
        self.__rutaAsignada = valor
        print("Ruta asignada")