import numpy as np
import csv
from claseMamas import Mama

class GestorMama:
    __listaMamas: np.ndarray
    __dimension: int
    __incremento: int
    __cantidad: int

    def __init__(self, dim=17):
        self.__dimension = dim
        self.__incremento = 3
        self.__cantidad = 0
        self.__listaMamas = np.empty(self.__dimension, dtype=Mama)

    def agregarMama(self, unaMama):
        if self.__cantidad == self.__dimension:
            print("\nSe solicitó espacio de almacenamiento.")
            self.__dimension += self.__incremento
            self.__listaMamas.resize(self.__dimension)
        self.__listaMamas[self.__cantidad] = unaMama
        self.__cantidad += 1
        print("Mamá cargada.")
    
    def cargarCSVMamas(self):
        archivo = open('Mamas.csv', encoding='utf-8')
        reader = csv.reader(archivo, delimiter=';')
        band = True
        for fila in reader:
            if band:
                band = False
            else:
                mama = Mama(fila[0], int(fila[1]), fila[2], fila[3])
                self.agregarMama(mama)
        archivo.close()

    # Inciso a)
    def mostrarInfoMama(self, dniMama, gestorNac):
        encontrado = False
        i = 0
        while not encontrado and i < self.__cantidad:
            if self.__listaMamas[i].getDNI() == dniMama:
                encontrado = True
                