# Nombre: Papeschi Gina
# DNI: 46407532
# Número de registro: E010-252

import csv
import numpy as np
from claseMovilidades import Movilidad

class GestorMovilidad:
    __listaMov: np.ndarray
    __dimension: int
    __incremento: int
    __cantidad: int

    def __init__(self, dim=4):
        self.__dimension = dim
        self.__incremento = 3
        self.__cantidad = 0
        self.__listaMov = np.empty(self.__dimension, dtype=Movilidad)

    def agregarMovilidad(self, unaMovilidad):
        if self.__cantidad == self.__dimension:
            print("Espacio de almacenamiento solicitado.")
            self.__dimension += self.__incremento
            self.__listaMov.resize(self.__dimension)
        self.__listaMov[self.__cantidad] = unaMovilidad
        self.__cantidad += 1
        print("Movilidad cargada.")

    def cargarCSVMovilidades(self):
        archivo = open('movilidades.csv', encoding='utf-8')
        reader = csv.reader(archivo, delimiter=';')
        band = True
        for fila in reader:
            if band:
                band = False
            else:
                mov = Movilidad(fila[0], fila[1], int(fila[2]), float(fila[3]), fila[4], fila[5])
                self.agregarMovilidad(mov)
        archivo.close()

    # Inciso A
    def listarMovilidades(self, patente, gestorGastos):
        encontrado = False
        i = 0
        while not encontrado and i < self.__cantidad:
            if self.__listaMov[i].getPatente() == patente:
                encontrado = True
                movilidad = self.__listaMov[i]
                print()
                print(f"Patente: {movilidad.getPatente()} Tipo: {movilidad.getTipo()} Capacidad de Carga: {movilidad.getCapacidadCarga()}")
                print(f"Importe Mensual de Patente: ${movilidad.getImporteMensual():.2f} Marca: {movilidad.getMarca()} Modelo: {movilidad.getModelo()}")

                gestorGastos.listarGastos(patente, movilidad.getImporteMensual())

            else:
                i += 1

        if not encontrado:
            print("\nERROR - No existe la patente ingresada.")

    # Inciso C
    def incisoC(self, fecha, gestorGastos):
        gestorGastos.ordenarGastos()
        print(f"\nListado de movilidades con gastos en la fecha {fecha}:")
        for i in range(self.__cantidad):
            total = gestorGastos.totalPorFechaYPatente(fecha, self.__listaMov[i].getPatente())
            
            if total > 0:
                print(f"- Patente: {self.__listaMov[i].getPatente()}")
                print(f"- Marca: {self.__listaMov[i].getMarca()}")
                print(f"- Modelo: {self.__listaMov[i].getModelo()}")
                print(f"- Total a pagar: ${total:.2f}")

