class Departamento:
    __id: int
    __NyA_propietario: str
    __num_piso: int
    __num_depto: int
    __cant_habitaciones: int
    __cant_banios: int
    __sup_cubierta: float

    def __init__(self, id, NyA, numP, numD, cantH, cantB, sup):
        self.__id = id
        self.__NyA_propietario = NyA
        self.__num_piso = numP
        self.__num_depto = numD
        self.__cant_habitaciones = cantH
        self.__cant_banios = cantB
        self.__sup_cubierta = sup
    
    def getID(self):
        return self.__id
    
    def getNyAProp(self):
        return self.__NyA_propietario
    
    def getNum_piso(self):
        return self.__num_piso
    
    def getNum_depto(self):
        return self.__num_depto
    
    def getCant_H(self):
        return self.__cant_habitaciones
    
    def getCant_B(self):
        return self.__cant_banios

    def getSupCubierta(self):
        return self.__sup_cubierta