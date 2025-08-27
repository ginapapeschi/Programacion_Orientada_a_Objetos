# Nombre: Papeschi Gina
# DNI: 46407532
# Número de registro: E010-252

import csv
from claseGastos import Gasto

class GestorGasto:
    __listaGastos: list

    def __init__(self):
        self.__listaGastos = []

    def agregarGasto(self, unGasto):
        self.__listaGastos.append(unGasto)
        print("Gasto cargado.")

    def cargarCSVGastos(self):
        archivo = open('gastosAbril2025.csv', encoding='utf-8')
        reader = csv.reader(archivo, delimiter=';')
        band = True
        for fila in reader:
            if band:
                band = False
            else:
                gasto = Gasto(fila[0], fila[1], float(fila[2]), fila[3])
                self.agregarGasto(gasto)
        archivo.close()

    # Inciso A
    def listarGastos(self, patente, importePatente):
        encabezadoImpreso = False
        totalGastos = 0

        for gasto in self.__listaGastos:
            if gasto.getPatente() == patente:
                fecha = gasto.getFecha()

                if fecha.split('-')[1] == '04':
                    if not encabezadoImpreso:
                        print("\nGastos:")
                        print(f"{'Fecha':<12} | {'Importe':<12} | {'Descripción'}")
                        encabezadoImpreso = True

                    print(f"{fecha:<12} | ${gasto.getImporte():<11.2f} | {gasto.getDescripcion()}")
                    totalGastos += gasto.getImporte()

        totalConPatente = totalGastos + importePatente
        print(f"\nTotal de Gastos (incluye Patente): ${totalConPatente:.2f}")

    # Inciso B
    def gastosEnElDia(self, fecha):
        total = 0
        tieneGasto = False

        print(f"\nGastos del día {fecha}:")

        for i in range (len(self.__listaGastos)):
            if self.__listaGastos[i].getFecha() == fecha:
                print(f"- {self.__listaGastos[i].getDescripcion()}: ${self.__listaGastos[i].getImporte():.2f}")
                total += self.__listaGastos[i].getImporte()
                tieneGasto = True
                
        if not tieneGasto:
            print("- El cliente no tuvo gastos en la fecha ingresada")
        else:
            print(f"Total a pagar: ${total:.2f}")

    # Inciso C
    def ordenarGastos(self):
        self.__listaGastos.sort()

    def totalPorFechaYPatente(self, fecha, patente):
        total = 0
        for gasto in self.__listaGastos:
            if gasto.getFecha() == fecha and gasto.getPatente() == patente:
                total += gasto.getImporte()

        return total



