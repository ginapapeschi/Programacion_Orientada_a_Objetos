from ClasePublicacion import Publicacion

class LibroImpreso (Publicacion):       # Herencia de la clase Publicación.
    __autor: str
    __fecha_edi: str
    __cant_pag: int

    def __init__ (self, **kwargs):
        super().__init__(kwargs['tit'], kwargs['cat'], kwargs['precio'])   # 'kwargs' es un diccionario que acepta cualquier nº de argumentos con nombre pasados a la función.
                                                                           # Importante que se respete la clave de cada palabra dentro de los corchetes. Corresponden a la misma clave que se asignó en los atributos de la SUPERCLASE.
        self.__autor = kwargs['nombreAutor']
        self.__fecha_edi = kwargs['fechaEdi']
        self.__cant_pag = kwargs['cantPag']

    def __str__ (self):
        return f'Título: {super().getTitulo()}\n Nombre del autor: {self.getNomAutor()}'    # getTitulo es un método de la SUPERCLASE Publicación.

    def getNomAutor(self):
        return self.__autor
    
    def getFechaEdicion(self):
        return self.__fecha_edi
    
    def getCantPag(self):
        return self.__cant_pag
    
