import numpy as np
import csv
from claseAtencion import Atencion

class ManejadorAtencion:
    __listaAt: np.ndarray
    __dimension: int
    __incremento: int
    __cantidad: int
    
    def __init__(self, dim=40, inc=10):
        self.__dimension = dim
        self.__incremento = inc
        self.__cantidad = 0
        self.__listaAt = np.empty(self.__dimension, dtype=Atencion)

    def agregarAtencion(self, unaAtencion):
        if self.__cantidad == self.__dimension:
            print("Espacio de almacenamiento solicitado.")
            self.__dimension += self.__incremento
            self.__listaAt.resize(self.__dimension)
        self.__listaAt[self.__cantidad] = unaAtencion
        self.__cantidad += 1

    def cargarCSVAtenciones(self):
        archivo = open('atenciones.csv', encoding='utf-8')
        reader = csv.reader(archivo, delimiter=';')
        band = True
        for fila in reader:
            if band:
                band = False
            else:
                atencion = Atencion(fila[0], str(fila[1]), float(fila[2]))
                self.agregarAtencion(atencion)
                print("Atención cargada.")
        archivo.close()

    def incisoA(self, fecha):
        cont = 0
        impTotal = 0
        for i in range(self.__cantidad):
            if self.__listaAt[i].getFecha() == fecha:
                cont += 1
                impTotal += self.__listaAt[i].getImporte()
        
        if cont > 0:
            print(f"\nLas atenciones realizadas en la fecha {fecha} fueron {cont}. Importe total a pagar: ${impTotal:.2f}.")
        else:
            print("\nNo se registraron atenciones para la fecha ingresada.")

    # Inciso B
    def contarAtenciones(self, dni):
        cont = 0
        for i in range(self.__cantidad):
            if self.__listaAt[i].getDNIAtencion() == dni:
                cont += 1
        
        return cont