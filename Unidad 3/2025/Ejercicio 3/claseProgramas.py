class Programa:
    __nombre: str
    __codigo: str
    __duracion: int

    def __init__(self, nom, cod, dur):
        self.__nombre = nom
        self.__codigo = cod
        self.__duracion = dur

    def __str__(self):
        return f"Programa {self.__nombre} - Código: {self.__codigo} - Duración: {self.__duracion}"

    def getNombre(self):
        return self.__nombre
    
    def getCodigo(self):
        return self.__codigo
    
    def getDuracion(self):
        return self.__duracion