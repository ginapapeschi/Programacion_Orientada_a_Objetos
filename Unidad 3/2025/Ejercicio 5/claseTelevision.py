from claseMedio import Medio

class Television(Medio):
    __canal: int
    __cantProgramas: int                                            # Cantidad de canales o programas
    __listaProgramas: list

    def __init__(self, nom, aud, canal, cant):
        super().__init__(nom, aud)
        self.__canal = canal
        self.__cantProgramas = cant
        self.__listaProgramas = []

    def agregarPrograma(self, unPrograma):
        self.__listaProgramas.append(unPrograma)
        print("Programa de televisión cargado.")

    # Inciso 4
    def buscarProgramaPorNombre(self, nom):
        encontrado = False
        i = 0
        television = None

        while i < len(self.__listaProgramas) and not encontrado:
            if self.__listaProgramas[i].getNombre().lower() == nom.lower():
                encontrado = True
                television = self
            
            else:
                i += 1
        
        return television

    def getHorariosPrograma(self, nom):
        encontrado = False
        i = 0

        while not encontrado and i < len(self.__listaProgramas):
            if self.__listaProgramas[i].getNombre().lower() == nom.lower():
                encontrado = True
                horarioInicio = self.__listaProgramas[i].getHorarioInicio()
                horarioFin = self.__listaProgramas[i].getHorarioFin()
                print(f"Horario de inicio: {horarioInicio} - Horario de finalización: {horarioFin}")
            
            else:
                i += 1

    # Inciso 5
    def mostrarProgramas(self):
        for programa in self.__listaProgramas:
            print(programa)

    def __str__(self):
        return f"{super().__str__()} - Cantidad de programas: {self.__cantProgramas}"   # LLama al str de la clase padre y agrega la información de la subclase

    def getCanal(self):
        return self.__canal

    def getCantProgramas(self):
        return self.__cantProgramas
    
    def getProgramas(self):
        return self.__listaProgramas