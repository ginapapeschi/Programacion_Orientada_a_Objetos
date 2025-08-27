from ClaseLadrillo import Ladrillo
import csv

class GestorLad:
    __listaGestorLad: list

    def __init__ (self):
        self.__listaGestorLad = []

    def agregarLadrillo(self, nuevo):
        self.__listaGestorLad.append(nuevo)

    def leerdatos(self):
        archivo = open('Ladrillos.csv')
        reader = csv.reader(archivo, delimiter = ';')
        band = True
        for fila in reader:
            if band:
                band = False
            else:
                self.agregarLadrillo(Ladrillo(int(fila[0]), int(fila[1]), float(fila[2]), float(fila[3])))
        archivo.close()

    def buscarID(self, xid):
        band = True
        i = 0
        pos = -1
        while i < len(self.__listaGestorLad) and band:
            if self.__listaGestorLad[i].getID() == xid:
                band = False
                pos = i
            else:
                i += 1
        return pos
            
    def mostrarDatosMateriales(self, id): # Ingrese el ID del ladrillo para detallar costo y características del material.
        pos = self.buscarID(id)
        if pos != -1:                     # Si se encontró el ladrillo en la lista de ladrillos. Uso pos para posicionarme en la lista con el ID buscado.
            print(f"Datos del ladrillo con ID {id}:")
            for material in self.__listaGestorLad[pos].__materiales:
                costo = self.__listaGestorLad[pos].__materiales.getCostoAdicional()
                caract = self.__listaGestorLad[pos].__materiales.getCaract()
        else:
            print(f"No se encontró un ladrillo con ID {id}")