class Cabana:
    __num: int
    __cantHabitaciones: int
    __cantCamasGrandes: int
    __cantCamasChicas: int
    __importe: float            # Por día

    def __init__(self, num, cantH, cantCG, cantCC, imp):
        self.__num = num
        self.__cantHabitaciones = cantH
        self.__cantCamasGrandes = cantCG
        self.__cantCamasChicas = cantCC
        self.__importe = imp

    def getNumero(self):
        return self.__num
    
    def getCantHabitaciones(self):
        return self.__cantHabitaciones
    
    def getCantCamasGrandes(self):
        return self.__cantCamasGrandes
    
    def getCantCamasChicas(self):
        return self.__cantCamasChicas
    
    def getImporte(self):
        return self.__importe
    
    def cantidadCamasTotal(self):
        return self.__cantCamasGrandes * 2 + self.__cantCamasChicas # Se suman la cantidad total de camas, multiplicando las camas grandes por 2 por ser de dos plazas (se calcula la cantidad de personas que pueden ser hospedadas en base a la cantidad total de camas)
    
    def __ge__ (self, otro):
        return int(self.cantidadCamasTotal()) >= int(otro)
