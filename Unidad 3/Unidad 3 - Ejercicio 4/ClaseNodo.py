from ClasePublicacion import Publicacion

class Nodo:
    _publicacion: Publicacion
    _siguiente: object

    def __init__(self, publicacion):
        self.__publicacion = publicacion
        self.__siguiente = None

    def setSiguiente(self, siguiente):
        self.__siguiente = siguiente

    def getDato(self):
        return self.__publicacion
    
    def getSiguiente(self):
        return self.__siguiente
    
    