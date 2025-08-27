import csv
import numpy as np
from claseCabañas import Cabaña

class GestorCabaña:
    __listaCab: np.ndarray
    __dimension: int
    __incremento: int
    __cantidad: int

    def __init__(self, dim=10):
        self.__dimension = dim
        self.__incremento = 3
        self.__cantidad = 0
        self.__listaCab = np.empty(self.__dimension, dtype=Cabaña)

    def agregarCabaña(self, unaCabaña):
        if self.__cantidad == self.__dimension:
            print("Se solicitó espacio de almacenamiento.")
            self.__dimension += self.__incremento
            self.__listaCab.resize(self.__dimension)
        self.__listaCab[self.__cantidad] = unaCabaña
        print("Cabaña cargada.")
        self.__cantidad += 1

    def cargarCSVCabañas(self):
        archivo = open('Cabañas.csv', encoding='utf-8')
        reader = csv.reader(archivo, delimiter=';')
        band = True
        for fila in reader:
            if band:
                band = False
            else:
                cabaña = Cabaña(int(fila[0]), int(fila[1]), int(fila[2]), int(fila[3]), float(fila[4]))
                self.agregarCabaña(cabaña)
        archivo.close()

    # Inciso A
    def cabañasSinReserva(self, cantH, gestorRes):
        hay = False
        print(f"\nCabañas con capacidad mayor a {cantH} y sin reserva:")
        for i in range(self.__cantidad):
            if self.__listaCab[i] >= cantH:
                numeroCabaña = self.__listaCab[i].getNumero()
                tieneReserva = gestorRes.tieneReserva(numeroCabaña)
                if tieneReserva == 0 and self.__listaCab[i]:
                    print(f"- Cabaña número {self.__listaCab[i].getNumero()}")
                    hay = True
        
        if not hay:
            print("- No hay cabañas con una capacidad mayor o igual a la ingresada y sin reserva.")


    # Inciso B
    def getImporteCabaña(self, numCabaña):
        encontrado = False
        importe = 0
        i = 0
        while not encontrado and i < self.__cantidad:
            if self.__listaCab[i].getNumero() == numCabaña:
                encontrado = True
                importe = self.__listaCab[i].getImporte()
            else:
                i += 1

        return importe