class Mama:
    __dni: int
    __edad: int
    __AyN: str

    def __init__(self, dni, edad, ayn):
        self.__dni = dni
        self.__edad = edad
        self.__AyN = ayn

    def __str__(self):
        return f"Apellido y nombre: {self.__AyN}\nEdad: {self.__edad}\nDNI: {self.__dni}"

    def getDNI(self):
        return self.__dni
    
    def getEdad(self):
        return self.__edad
    
    def getAyN(self):
        return self.__AyN