class Carrera:
    __codigoC: int
    __nomC: str
    __titulo: str
    __duracion: str
    __nivel: str
    __codFacu: int

    def __init__(self, cod, nom, titulo, dur, niv, codF):
        self.__codigoC = cod
        self.__nomC = nom
        self.__titulo = titulo
        self.__duracion = dur
        self.__nivel = niv
        self.__codFacu = codF

    def __str__(self):
        return self.__nomC

    def getNombreCarrera(self):
        return self.__nomC

    def __lt__(self, otraCarrera):
        return self.getNombreCarrera() < otraCarrera.getNombreCarrera()

    def getCodigoFacu(self):
        return self.__codFacu