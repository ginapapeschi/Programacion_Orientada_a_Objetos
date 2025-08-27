import csv
from claseMedios import Medio
from clasePrensaEscrita import PrensaEscrita
from claseRadios import Radio

class Control:
    __listaMedios: list

    def __init__(self):
        self.__listaMedios = []

    def agregarMedio(self, unMedio):
        self.__listaMedios.append(unMedio)
        print("Medio agregado")

    def cargarCSV(self):
        archivoMedios = open('Medios.csv', encoding='utf-8')
        readerM = csv.reader(archivoMedios, delimiter=',')
        archivoProgramas = open('Programas.csv', encoding='utf-8')
        readerP = csv.reader(archivoProgramas, delimiter=',')
        listaProgramas = list(readerP)
        for filaM in readerM:
            if filaM[0] == 'R':
                radio = Radio(filaM[1], int(filaM[2]), filaM[3])
                self.agregarMedio(radio)
                for filaP in listaProgramas:
                    if filaP[0].strip() == filaM[3].strip():
                        radio.agregarPrograma(filaP[1], filaP[2], filaP[3])
            
            elif filaM[0] == 'P':
                prensa = PrensaEscrita(filaM[1], int(filaM[2]), filaM[3], int(filaM[4]))
                self.agregarMedio(prensa)

        archivoMedios.close()
        archivoProgramas.close()

    # Inciso a
    def agregarManual(self, tipoMedio):
        if tipoMedio.lower() in ['prensa', 'radio']:
            nombre = input("Ingrese el nombre del medio: ")
            audiencia = int(input("Ingrese la audiencia: "))

            if tipoMedio.lower() == 'prensa':
                periodicidad = input("Ingrese la periodicidad: ")
                cantSecciones = int(input("Ingrese la cantidad de secciones: "))
                medio = PrensaEscrita(nombre, audiencia, periodicidad, cantSecciones)
            
            elif tipoMedio.lower() == 'radio':
                frecuencia = input("Ingrese la frecuencia: ")
                medio = Radio(nombre, audiencia, frecuencia)

            self.agregarMedio(medio)

        else:
            print("\nERROR - Medio ingresado no válido")

    # Inciso b
    def incisoB(self, nomPrograma):
        programa = None
        i = 0
        while programa is None and i < len(self.__listaMedios):
            if isinstance(self.__listaMedios[i], Radio):
                programa = self.__listaMedios[i].buscarProgramaPorNombre(nomPrograma)

                if programa:
                    print(f"\n{self.__listaMedios[i].__class__.__name__.capitalize()} {self.__listaMedios[i].getNombre().capitalize()} | {self.__listaMedios[i].getFrecuencia()}")
                    print(f"Horario de inicio de transmisión: {programa.getHoraInicio().strftime("%H:%M")}hs")

            i += 1
        
        if programa is None:
            raise ValueError("\nERROR - Programa ingresado no encontrado")
        
    # Inciso c
    def mostrarMedios(self):
        print()
        print("----- MEDIOS -----".center(25))
        for medio in self.__listaMedios:
            print()
            if isinstance(medio, Radio):
                print(f"Radio {medio.getNombre()}".center(25))
            else:
                print(f"Revista {medio.getNombre()}".center(25))
            print(f"Audiencia estimada: {medio.getAudiencia()}")
            print(f"Índice de audiencia: {medio.getIndiceAudiencia():.0f}")
