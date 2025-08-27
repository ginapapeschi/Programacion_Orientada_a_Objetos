class Mama:
    __dni: str
    __edad: int
    __apellido: str
    __nombre: str

    def __init__(self, dni, edad, ap, nom):
        self.__dni = dni
        self.__edad = edad
        self.__apellido = ap
        self.__nombre = nom

    def getDNI(self):
        return self.__dni
    
    def getEdad(self):
        return self.__edad
    
    def getApellido(self):
        return self.__apellido
    
    def getNombre(self):
        return self.__nombre