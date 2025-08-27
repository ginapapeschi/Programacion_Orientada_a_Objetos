class Medio:
    __nombre: str
    __audiencia: int

    def __init__(self, nom, aud):
        self.__nombre = nom
        self.__audiencia = aud

    def __str__(self):
        return f"Nombre: {self.__nombre} - Audiencia: {self.__audiencia}"

    def getNombre(self):
        return self.__nombre
    
    def getAudiencia(self):
        return self.__audiencia
    