class Cabaña:
    __num: int
    __cantHabitaciones: int
    __cantCamasGrandes: int
    __cantCamasChicas: int
    __importeDia: float

    def __init__(self, n, cantH, cantG, cantC, imp):
        self.__num = n
        self.__cantHabitaciones = cantH
        self.__cantCamasGrandes = cantG
        self.__cantCamasChicas = cantC
        self.__importeDia = imp

    def __ge__(self, cantidad):
        capacidad = self.getCantCamasGrandes() * 2 + self.getCantCamasChicas()
        return capacidad >= cantidad

    def getNumero(self):
        return self.__num
    
    def getCantHabitaciones(self):
        return self.__cantHabitaciones
    
    def getCantCamasGrandes(self):
        return self.__cantCamasGrandes
    
    def getCantCamasChicas(self):
        return self.__cantCamasChicas
    
    def getImporte(self):
        return self.__importeDia