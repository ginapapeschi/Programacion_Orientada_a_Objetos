class Nodo:
    __dato: object
    __siguiente: object

    def __init__(self, dato):
        self.__dato = dato
        self.__siguiente = None

    def getDato(self):
        return self.__dato
    
    def getSiguiente(self):
        return self.__siguiente
    
    def setSiguiente(self, sig):
        self.__siguiente = sig