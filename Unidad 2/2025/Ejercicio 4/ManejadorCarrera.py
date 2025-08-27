import numpy as np
import csv
from claseCarrera import Carrera

class manejadorCarrera:
    __listaC: np.ndarray
    __cantidad: int
    __dimension: int
    __incremento: int

    def __init__(self, dim=40):
        self.__cantidad = 0
        self.__dimension = dim
        self.__incremento = 5
        self.__listaC = np.empty(self.__dimension, dtype=Carrera)

    def agregarCarrera(self, unaCarrera):
        if self.__cantidad == self.__dimension:
            print("\nSe solicitó espacio de almacenamiento.")
            self.__dimension += self.__incremento
            self.__listaC.resize(self.__dimension)
        
        self.__listaC[self.__cantidad] = unaCarrera
        self.__cantidad += 1

    def cargarCSVCarrera(self):
        archivo = open('Carreras.csv')
        reader = csv.reader(archivo, delimiter=';')
        band = True
        for fila in reader:
            if band:
                band = False
            else:
                carrera = Carrera(int(fila[0]), fila[1], fila[2], fila[3], fila[4], int(fila[5]))
                self.agregarCarrera(carrera)
                print("Carrera cargada.")
        archivo.close()

    def incisoC(self, nomC, manejadorF):
        encontrado = False
        i = 0
        nomFacultad = None
        while not encontrado and i < self.__cantidad:
            if self.__listaC[i].getNombreCarrera() == nomC:
                encontrado = True
                codigoAsociado = self.__listaC[i].getCodigoFacu()
                nomFacultad = manejadorF.buscarFacultad(codigoAsociado)
            else:
                i += 1
        
        if encontrado:
            if nomFacultad:
                print(f"\nEl nombre de la facultad donde se dicta {nomC} es {nomFacultad}.")
            else:
                print(f"\nNo se encontró facultad donde se dicte {nomC}.")
        else:
            print(f"\nNo se encontró la carrera ingresada.")

    # Inciso D
    def totalCarreras(self):
        return self.__cantidad
    
    def getCodigoFacultadPorCarreraIndice(self, j):
        return self.__listaC[j].getCodigoFacu()
    
    # Inciso E
    def ordenarCarreras(self):
        self.__listaC.sort()
    
    def printCarrera(self, j):
        print(self.__listaC[j])