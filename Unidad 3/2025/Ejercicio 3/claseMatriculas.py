from claseEmpleados import Empleado
from claseProgramas import Programa

class Matricula:
    __fecha: str
    __empleados: object
    __programas: object

    def __init__(self, fecha, empleados, programas):
        self.__fecha = fecha
        self.__empleados = empleados
        self.__programas = programas

    def __str__(self):
        return f"{self.__empleados} - {self.__programas} - {self.__fecha}"

    def getEmpleado(self):
        return self.__empleados
    
    def getPrograma(self):
        return self.__programas
    
    def getFecha(self):
        return self.__fecha