import csv
from claseProgramas import Programa

class GestorPrograma:
    __listaProgramas: list

    def __init__(self):
        self.__listaProgramas = []

    def agregarPrograma(self, unPrograma):
        self.__listaProgramas.append(unPrograma)
        print("Programa cargado")

    def cargarCSVProgramas(self):
        archivo = open('programas.csv', encoding='utf-8')
        reader = csv.reader(archivo, delimiter=';')
        next(reader)
        for fila in reader:
            programa = Programa(fila[0], fila[1], int(fila[2]))
            self.agregarPrograma(programa)
        archivo.close()

    def buscarPrograma(self, nomPrograma):
        i = 0
        while i < len(self.__listaProgramas):
            if self.__listaProgramas[i].getNombre().lower() == nomPrograma.lower():
                return self.__listaProgramas[i]
            
            else:
                i += 1

