import csv
from claseNacimientos import Nacimiento

class GestorNacimiento:
    __listaNac: list

    def __init__(self):
        self.__listaNac = []

    def agregarNacimiento(self, unNacimiento):
        self.__listaNac.append(unNacimiento)
        print("Nacimiento cargado.")

    def cargarCSVNacimientos(self):
        archivo = open('Nacimientos.csv', encoding='utf-8')
        reader = csv.reader(archivo, delimiter=';')
        band = True
        for fila in reader:
            if band:
                band = False
            else:
                nacimiento = Nacimiento(fila[0], fila[1], fila[2], fila[3], float(fila[4]), float(fila[5]))
                self.agregarNacimiento(nacimiento)
        archivo.close()
        