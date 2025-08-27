from claseCabanas import Cabana
import csv
import numpy as np

class GestorCabana:
    __dimension: int
    __incremento: int
    __cantidad: int
    __lista: np.ndarray

    def __init__(self):
        self.__dimension = 10       # Porque el PDF ya indica que el complejo tiene 10 cabañas.
        self.__incremento = 1
        self.__cantidad = 0
        self.__lista = np.empty(self.__dimension, dtype=Cabana)

    def agregarCabana(self, unaCabana):
        if self.__cantidad == self.__dimension:
            print("\nSe solicitó espacio de almacenamiento.")
            self.__dimension += self.__incremento
            self.__lista.resize(self.__dimension)
        self.__lista[self.__cantidad] = unaCabana
        self.__cantidad += 1

    def leerCSVCabana(self):
        archivo = open("Cabañas.csv")
        reader = csv.reader(archivo, delimiter=";")
        next(reader)
        for fila in reader:
            cabana = (Cabana(int(fila[0]), int(fila[1]), int(fila[2]), int(fila[3]), float(fila[4])))
            self.agregarCabana(cabana)
        archivo.close()
        print("\nCabañas cargadas con éxito.")

    def mostrarCabanaCapacidad(self, cantHuespedes, gestorReserva):
        print("\nLISTA DE CABAÑAS:")
        i = 0
        while i < len(self.__lista):
            if self.__lista[i].cantidadCamasTotal() >= cantHuespedes and not gestorReserva.tieneReserva(self.__lista[i].getNumero()):
                print(f"Número de cabaña con capacidad para {cantHuespedes} huéspedes: Cabaña nº{self.__lista[i].getNumero()}")
            i += 1

    def importeDiario(self, numCabanaAsignada):
        i = 0
        while i < len(self.__lista):
            if self.__lista[i].getNumero() == numCabanaAsignada:
                return round(self.__lista[i].getImporte())
            i += 1