from datetime import datetime
from claseProgramas import Programa
from claseMedios import Medio

class Radio(Medio):
    __frecuencia: str
    __listaProgramas: list

    def __init__(self, nom, aud, frec):
        super().__init__(nom, aud)
        self.__frecuencia = frec
        self.__listaProgramas = []

    def agregarPrograma(self, nom, horaI, horaF):
        horaIDatetime = datetime.strptime(horaI, "%H:%M").time()
        horaFDatetime = datetime.strptime(horaF, "%H:%M").time()
        if horaIDatetime < horaFDatetime:
            unPrograma = Programa(nom, horaIDatetime, horaFDatetime)
            self.__listaProgramas.append(unPrograma)
            print("Programa agregado")
        else:
            raise ValueError("\nERROR - Horario incorrecto")

    def __str__(self):
        return f"{super().__str__()} - Frecuencia: {self.__frecuencia}"
    
    # Inciso b
    def buscarProgramaPorNombre(self, nomPrograma):
        i = 0
        programa = None
        
        while programa is None and i < len(self.__listaProgramas):
            if self.__listaProgramas[i].getNombre().strip().lower() == nomPrograma.strip().lower():
                programa = self.__listaProgramas[i]
            
            else:
                i += 1
                
        return programa

    def mostrarProgramas(self):
        print("\nProgramas:")
        for programa in self.__listaProgramas:
            print("- ", end="")
            print(programa)

    def getFrecuencia(self):
        return self.__frecuencia
    
    def getIndiceAudiencia(self):
        cantProgramas = len(self.__listaProgramas)
        if cantProgramas > 0:
            resultado = super().getAudiencia() / cantProgramas
        else:
            resultado = 0

        return resultado