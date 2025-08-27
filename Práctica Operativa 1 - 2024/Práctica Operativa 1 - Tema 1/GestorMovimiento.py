from ClaseMovimiento import Movimiento
import csv
import numpy as np

class GestorMov:
    __dimension: int
    __cantidad: int
    __incremento: int
    __listaMov: np.ndarray

    def __init__(self):         # se carga primero primero una columna, después las otras, por el resize
        self.__dimension = 21   # cantidad de movimientos (filas)
        self.__incremento = 5   # cantidad de datos (columnas), se usa para el resize cuando dimensión == incremento (o sea, llega al final de la lista)
        self.__cantidad = 0     # contador que incrementa al añadir un movimiento
        self.__listaMov = np.empty(self.__dimension, dtype = Movimiento)
    
    def agregarMovimiento(self, nuevoMov):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__listaMov.resize(self.__dimension)
        else:
            self.__listaMov[self.__cantidad] = nuevoMov
            self.__cantidad += 1

    def leerdatos(self):
        archivo = open('MovimientosAbril2024.csv')
        reader = csv.reader(archivo, delimiter = ';')
        band = True
        for fila in reader:
            if band:
                band = False
            else:
                self.agregarMovimiento(Movimiento(int(fila[0]), fila[1], fila[2], fila[3], float(fila[4])))
        archivo.close()
    
    def buscaTarjeta(self, GC):
        print("\n")
        num_t = int(input("Ingrese número de tarjeta: "))
        existe = False
        i = 0
        while i < len(GC._GestorCli__listaCli) and existe is False:
            if num_t == GC._GestorCli__listaCli[i].getNro_tarjeta():
                existe = True
                AyN = GC._GestorCli__listaCli[i].getApellido() + ' ' + GC._GestorCli__listaCli[i].getNombre()
            else:
                i += 1
        if existe is False:
            print("No se encontró la tarjeta ingresada")
        else:
            j = 0
            nohayMov = True
            while j < len(self.__listaMov) and nohayMov:
                if num_t == self.__listaMov[j].getNro_tarjeta():
                    nohayMov= False
                else:
                    j += 1
            if nohayMov is False:
                print("El cliente {} realizó movimientos con la tarjeta ingresada.".format(AyN))
            else:
                print(f"El nombre del cliente que no tuvo movimientos es: {AyN}")
    
    def ordenarMov(self):
       self.__listaMov = np.sort(self.__listaMov)
       print("\n")
       print("Se ordenó la lista de movimientos.")
    
    def listarMov(self):
        print("\n")
        print("Listado de movimientos ordenados por número de tarjeta:")
        for i in (self.__listaMov):
            print(i)