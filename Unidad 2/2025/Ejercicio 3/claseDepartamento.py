class Departamento:
    __identificador: int
    __nombreDepto: str

    def __init__(self, id, nom):
        self.__identificador = id
        self.__nombreDepto = nom
    
    def getNombreDepto(self):
        return self.__nombreDepto
    
    def getID(self):
        return self.__identificador