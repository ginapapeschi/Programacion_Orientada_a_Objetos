class Gammer:
    __idJugador: int
    __dni: int
    __nombre: str
    __apellido: str
    __alias: str
    __plan: str
    __importeBase: float
    __tiempoLimite: int
    
    def __init__ (self, id, dni, nom, ap, alias, plan, imp, tpo):
        self.__idJugador = id
        self.__dni =  dni
        self.__nombre = nom
        self.__apellido = ap
        self.__alias = alias
        self.__plan = plan
        self.__importeBase = imp
        self.__tiempoLimite = tpo
    
    def __str__(self):
        return f"ID Jugador: {self.__idJugador}\nDNI: {self.__dni}\nNombre y apellido: {self.__nombre + self.__apellido}\nAlias: {self.__alias}\nPlan: {self.__plan}"

    def getIDJugador(self):
        return self.__idJugador
    
    def getDNI(self):
        return self.__dni
    
    def getNombre(self):
        return self.__nombre
    
    def getApellido(self):
        return self.__apellido
    
    def getAlias(self):
        return self.__alias
    
    def getPlan(self):
        return self.__plan
    
    def getImporteBase(self):
        return self.__importeBase
    
    def getTiempoLimite(self):
        return self.__tiempoLimite