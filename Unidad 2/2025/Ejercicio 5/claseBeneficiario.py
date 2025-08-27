class Beneficiario:
    __dni: str
    __nombre: str
    __apellido: str
    __carrera: str
    __siglaFacultad: str
    __anioCursa: int
    __promedio: float
    __IDBeca: int

    def __init__(self, dni, nom, ap, car, sigla, anio, prom, id):
        self.__dni = dni
        self.__nombre = nom
        self.__apellido = ap
        self.__carrera = car
        self.__siglaFacultad = sigla
        self.__anioCursa = anio
        self.__promedio = prom
        self.__IDBeca = id

    def __lt__(self, otro):
        return self.__siglaFacultad > otro.getSiglaF()

    def getDNI(self):
        return self.__dni
    
    def getNombre(self):
        return self.__nombre
    
    def getApellido(self):
        return self.__apellido
    
    def getCarrera(self):
        return self.__carrera
    
    def getSiglaF(self):
        return self.__siglaFacultad
    
    def getAnio(self):
        return self.__anioCursa
    
    def getPromedio(self):
        return self.__promedio
    
    def getIDBeca(self):
        return self.__IDBeca