from ClaseMaterial import Material
import csv

class GestorMat:
    __listaGestorMat: list

    def __init__ (self):
        self.__listaGestorMat = []

    def agregarMaterial(self, nuevo):
        self.__listaGestorMat.append(nuevo)

    def leerdatos(self):
        archivo = open('Materiales.csv')
        reader = csv.reader(archivo, delimiter = ';')
        band = True
        for fila in reader:
            if band:
                band = False
            else:
                self.agregarMaterial(Material(int(fila[0]), (fila[1]), float(fila[2]), float(fila[3])))
        archivo.close()