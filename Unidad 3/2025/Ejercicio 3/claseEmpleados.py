class Empleado:
    __NyA: str
    __idEmpleado: int
    __puesto: str

    def __init__(self, nya, id, puesto):
        self.__NyA = nya
        self.__idEmpleado = id
        self.__puesto = puesto
        
    def __str__(self):
        return f"Empleado {self.__NyA} - ID: {self.__idEmpleado} - Puesto: {self.__puesto}"

    def getNombre(self):
        return self.__NyA
    
    def getID(self):
        return self.__idEmpleado
    
    def getPuesto(self):
        return self.__puesto