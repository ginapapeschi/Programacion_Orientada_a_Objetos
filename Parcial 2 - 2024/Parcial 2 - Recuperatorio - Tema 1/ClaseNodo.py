from ClaseEquipo import Equipo

class Nodo:
    __equipo: Equipo 
    __siguiente: object
    
    def __init__(self, eq):
        self.__equipo = eq
        self.__siguiente = None

    def setSiguiente(self, siguiente):
        self.__siguiente = siguiente

    def getSiguiente(self):
        return self.__siguiente
    
    def getDato(self):
        return self.__equipo
    