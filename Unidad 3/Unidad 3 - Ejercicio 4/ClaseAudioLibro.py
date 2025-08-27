from ClasePublicacion import Publicacion

class AudioLibro (Publicacion):         # Herencia de la clase Publicación
    __tiempoRep: float
    __nomNarrador: str

    def __init__(self, **kwargs):
        super().__init__(kwargs['tit'], kwargs['cat'], kwargs['precio'])    # Es recomendable inicializar los atributos de la SUPERCLASE en la SUBCLASE siempre.
        self.__tiempoRep = kwargs['tiempoReproduccion']
        self.__nomNarrador = kwargs['nombreNarrador']
    
    def getTiempoReproduccion(self):
        return self.__tiempoRep
    
    def getNomNarrador(self):
        return self.__nomNarrador
    

    