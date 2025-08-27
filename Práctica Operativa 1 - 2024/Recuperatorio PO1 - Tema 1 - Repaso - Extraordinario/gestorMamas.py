from claseMamas import Mama
import csv
import numpy as np

class gestorMama:
    __dimension: int
    __cantidad: int
    __incremento: int
    __lista: np.ndarray

    def __init__(self):
        self.__dimension = 0
        self.__cantidad = 0
        self.__incremento = 1
        self.__lista = np.empty(self.__dimension, dtype=Mama)

    def agregarMama(self, unaMama):
        if self.__cantidad == self.__dimension:
            print("Se solicitó espacio de almacenamiento")
            self.__dimension += self.__incremento
            self.__lista.resize(self.__dimension)
        self.__lista[self.__cantidad] = unaMama
        self.__cantidad += 1

    def leerCSV(self):
        archivo = open("Mamas.csv")
        reader = csv.reader(archivo, delimiter=";")
        next(reader)
        for fila in reader:
            mama = (Mama(int(fila[0]), int(fila[1]), fila[2]))
            self.agregarMama(mama)
        archivo.close()
        print("\nMamás cargadas exitosamente.")

    def buscarDNI(self, dni, gestorNacimiento):
        i = 0
        band = True
        while i < len(self.__lista) and band:
            if self.__lista[i].getDNI() == dni:
                band = False
                print(f"""
Apellido y nombre: {self.__lista[i].getAyN()}
Edad: {self.__lista[i].getEdad()} """)
                gestorNacimiento.buscarDNIMama(dni)
            i += 1

    def mostrarMama(self, dni):
        print("\nDatos de la mamá:")
        i = 0
        band = True
        while i < len(self.__lista) and band:
            if self.__lista[i].getDNI() == dni:
                print(self.__lista[i])
                band = False
            i += 1
