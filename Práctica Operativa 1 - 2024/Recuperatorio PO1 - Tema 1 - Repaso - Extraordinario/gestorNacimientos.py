from claseNacimientos import Nacimiento
import csv

class gestorNacimiento:
    __lista: list

    def __init__(self):
        self.__lista = []

    def agregarNacimiento(self, unNacimiento):
        self.__lista.append(unNacimiento)

    def leerCSV(self):
        archivo = open("Nacimientos.csv")
        reader = csv.reader(archivo, delimiter=";")
        next(reader)
        for fila in reader:
            nacimiento = (Nacimiento(int(fila[0]), fila[1], fila[2], fila[3], float(fila[4].replace(",", ".")), float(fila[5])))
            self.agregarNacimiento(nacimiento)
        archivo.close()
        print("\nNacimientos cargados exitosamente.")

    def buscarDNIMama(self, dni):
        i = 0
        band = True
        while i < len(self.__lista) and band:
            if self.__lista[i].getDNIMama() == dni:
                band = False
                print(f"""Tipo de parto: {self.__lista[i].getTipoParto()}
Bebé/s
Peso       Altura:
{self.__lista[i].getPeso()}kg       {round(self.__lista[i].getAltura())}cm
                      """)
            i += 1

    def mostrarDatosPartoMultiple(self, gestorMama):
        print("\nMAMÁS CON PARTOS MÚLTIPLES")
        i = 0
        while i < len(self.__lista):
            j = i+1
            while j < len(self.__lista):
                if i != j and self.__lista[i] == self.__lista[j]:
                    gestorMama.mostrarMama(self.__lista[i].getDNIMama())
                j += 1
            i += 1