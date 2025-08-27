class Habitacion:
    __numero: int
    __piso: int
    __tipoHabitacion: str
    __precioNoche: float
    __disponibilidad: bool

    def __init__(self, num, piso, tipo, precio, disp):
        self.__numero = num
        self.__piso = piso
        self.__tipoHabitacion = tipo
        self.__precioNoche = precio
        self.__disponibilidad = disp

    def setDisponibilidad(self, disp):
        self.__disponibilidad = disp

    def getNumero(self):
        return self.__numero
    
    def getPiso(self):
        return self.__piso
    
    def getTipo(self):
        return self.__tipoHabitacion
    
    def getPrecio(self):
        return self.__precioNoche
    
    def getDisponibilidad(self):
        return self.__disponibilidad