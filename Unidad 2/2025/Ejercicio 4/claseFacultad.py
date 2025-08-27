class Facultad:
    __codigoF: int
    __nomF: str
    __direccion: str
    __localidad: str
    __tel: str

    def __init__(self, cod, nom, dir, loc, tel):
        self.__codigoF = cod
        self.__nomF = nom
        self.__direccion = dir
        self.__localidad = loc
        self.__tel = tel

    def getCodigoFacultad(self):
        return self.__codigoF
    
    def getNombreFacultad(self):
        return self.__nomF