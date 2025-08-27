import csv
import numpy as np
from claseMovimientos import Movimiento

class GestorMovimientos:
    __listaMov: np.ndarray
    __dimension: int
    __incremento: int
    __cantidad: int

    def __init__(self, dim=21):
        self.__dimension = dim
        self.__incremento = 5
        self.__cantidad = 0
        self.__listaMov = np.empty(self.__dimension, dtype=Movimiento)

    def agregarMovimiento(self, unMovimiento):
        if self.__cantidad == self.__dimension:
            print("Espacio de almacenamiento solicitado.")
            self.__dimension += self.__incremento
            self.__listaMov.resize(self.__dimension)
        self.__listaMov[self.__cantidad] = unMovimiento
        self.__cantidad += 1
        print("Movimiento cargado.")

    def cargarCSVMov(self):
        archivo = open('MovimientosAbril2024.csv', encoding='utf-8')
        reader = csv.reader(archivo, delimiter=';')
        band = True
        for fila in reader:
            if band:
                band = False
            else:
                mov = Movimiento(int(fila[0]), fila[1], fila[2], fila[3], float(fila[4]))
                self.agregarMovimiento(mov)
        archivo.close()

    # Inciso A
    def getSaldoTotalMovimientos(self, numTarjeta, saldo):
        for i in range(self.__cantidad):
            if self.__listaMov[i].getNumTarjeta() == numTarjeta:
                if self.__listaMov[i].getTipoMov().lower() == 'c':
                    saldo+= self.__listaMov[i].getImporte()
                
                elif self.__listaMov[i].getTipoMov().lower() == 'p':
                    saldo -= self.__listaMov[i].getImporte()
        
        return saldo
    
    def mostrarListado(self, numTarjeta):
        print("Movimientos")
        print(f"{'Fecha':<15} | {'Descripción':<25} | {'Importe':<12} | {'Tipo de movimiento':<20}")
        for i in range(self.__cantidad):
            if self.__listaMov[i].getNumTarjeta() == numTarjeta:
                print(self.__listaMov[i])

    # Inciso B
    def tuvoMovimientosAbril(self, numTarjeta):
        tuvo = 0
        for i in range(self.__cantidad):
            if self.__listaMov[i].getNumTarjeta() == numTarjeta:
                fecha = self.__listaMov[i].getFecha()
                mes = int(fecha.split("/")[1])
                if mes == 4:
                    tuvo = 1

        return tuvo
    
    # Inciso C
    def ordenarMovimientos(self):
        self.__listaMov.sort()
        print("\nMovimientos ordenados.")