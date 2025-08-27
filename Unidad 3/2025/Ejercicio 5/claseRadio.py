from claseMedio import Medio

class Radio(Medio):
    __nomEmisora: str
    __frecuencia: str
    __listaProgramas: list

    def __init__(self, nom, aud, emi, frec):
        super().__init__(nom, aud)
        self.__nomEmisora = emi
        self.__frecuencia = frec
        self.__listaProgramas = []

    def agregarPrograma(self, unPrograma):
        self.__listaProgramas.append(unPrograma)
        print("Programa de radio cargado.")

    def mostrarProgramas(self):
        for programa in self.__listaProgramas:
            print(programa)

    def __str__(self):
        return f"{super().__str__()} - Frecuencia: {self.__frecuencia}"

    def getEmisora(self):
        return self.__nomEmisora

    def getFrecuencia(self):
        return self.__frecuencia
    
    def getProgramas(self):
        return self.__listaProgramas