class Persona:
    __nombre: str
    __apellido: str
    __edad: int
    __dni: str

    def __init__(self, nom, ap, ed, dni):
        self.__nombre = nom
        self.__apellido = ap
        self.__edad = ed
        self.__dni = dni

    def __str__(self):
        return f"- {self.__nombre} {self.__apellido} - Edad: {self.__edad} - DNI: {self.__dni}"

    def getNombre(self):
        return self.__nombre
    
    def getApellido(self):
        return self.__apellido
    
    def getEdad(self):
        return self.__edad
    
    def getDNI(self):
        return self.__dni