import numpy as np
from claseMovimientos import Movimiento
import csv

class GestorMovimiento:
    __cantidad: int
    __dimension: int
    __incremento: int
    __lista: np.ndarray
    
    def __init__(self):
        self.__cantidad = 0
        self.__dimension = 0
        self.__incremento = 1
        self.__lista = np.empty(self.__dimension, dtype=Movimiento)

    def agregarMovimiento(self, unMovimiento):
        if self.__cantidad == self.__dimension:
            print("Se solicitó espacio de almacenamiento.")
            self.__dimension += self.__incremento
            self.__lista.resize(self.__dimension)
        self.__lista[self.__cantidad] = unMovimiento
        self.__cantidad += 1
    
    def leerCSV(self):
        archivo = open("MovimientosAbril2024.csv")
        reader = csv.reader(archivo, delimiter=";")
        next(reader)
        for fila in reader:
            movimiento = (Movimiento(int(fila[0]), fila[1], fila[2], fila[3], float(fila[4])))
            self.agregarMovimiento(movimiento)
        print("\nMovimientos cargados exitosamente.\n")
        archivo.close()

    def buscarNumTarjeta(self, numTarjetaC, saldoAnterior):
        i = 0
        sumCreditos:float = 0
        sumPagos:float = 0
        print("\nMOVIMIENTOS:")
        print(f"""
            Fecha:           Descripción:       Importe:        Tipo de movimiento: 
                    """)
        while i < len(self.__lista):
            if self.__lista[i].getNumTarjeta() == numTarjetaC:
                if self.__lista[i].getTipoMovimiento() == "C":
                    sumCreditos += self.__lista[i].getImporte()
                    print(f"""
            {self.__lista[i].getFecha()} {self.__lista[i].getDescripcion()}  ${round(self.__lista[i].getImporte())}  {self.__lista[i].getTipoMovimiento()}
                    """)
                elif self.__lista[i].getTipoMovimiento() == "P":
                    sumPagos += self.__lista[i].getImporte()
                    print(f"""
            {self.__lista[i].getFecha()} {self.__lista[i].getDescripcion()}  ${round(self.__lista[i].getImporte())}  {self.__lista[i].getTipoMovimiento()}
                    """)
            i+=1

        saldoAnterior += sumCreditos
        saldoAnterior -= sumPagos
        return saldoAnterior

    def movimientosAbril(self, numTarjeta, gestorCliente):
        i = 0
        band = True
        while i < len(self.__lista) and band:
            if self.__lista[i].getNumTarjeta() == numTarjeta:
                fecha = self.__lista[i].getFecha()
                fecha = fecha.split("/")
                mes = fecha[1]
                if mes == "4":
                    band = False
            i += 1
        if band:
            AyN = gestorCliente.buscarNumTarjeta(numTarjeta)
            print(f"\nEl cliente que no tuvo movimientos en abril de 2024 es: {AyN}")
        else:
            print("\nEl cliente sí tuvo movimientos en abril de 2024.")

    def ordenarPorNroTarjeta(self):
        self.__lista.sort()
        print("\nLISTA ORDENADA POR NÚMERO DE TARJETA:")
        for movimiento in self.__lista:
            print(f"\nNúmero de tarjeta: {movimiento.getNumTarjeta()}") 