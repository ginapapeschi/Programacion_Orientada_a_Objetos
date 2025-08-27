import csv
import numpy as np
from claseFacultad import Facultad

class manejadorFacultad:
    __listaF: np.ndarray
    __cantidad: int
    __dimension: int        # Capacidad inicial del arreglo
    __incremento: int       # Cantidad de posiciones que se agregan si el arreglo se queda sin espacio
    
    def __init__(self, dim=5):
        self.__cantidad = 0
        self.__dimension = dim
        self.__incremento = 3
        self.__listaF = np.empty(self.__dimension, dtype=Facultad)

    def agregarFacultad(self, unaFacu):
        if self.__cantidad == self.__dimension: # Evalúa si la cantidad de objetos almacenados alcanzó la capacidad máxima del arreglo
            print("\nSe solicitó espacio de almacenamiento.")
            self.__dimension += self.__incremento   # Se incrementa la dimensión en una estimación de futuras inserciones
            self.__listaF.resize(self.__dimension)  # Se redimensiona la lista para que pueda contener más elementos

        self.__listaF[self.__cantidad] = unaFacu    # Se almacena el nuevo objeto en la primera posición libre
        self.__cantidad += 1                        # Se actualiza la cantidad total de objetos almacenados

    def cargarCSVFacultad(self):
        archivo = open('Facultades.csv')
        reader = csv.reader(archivo, delimiter=';')
        band = True
        for fila in reader:
            if band:
                band = False
            else:
                facu = Facultad(int(fila[0]), fila[1], fila[2], fila[3], fila[4])
                self.agregarFacultad(facu)
                print("Facultad cargada.")
        archivo.close()
    
    # Inciso C
    def buscarFacultad(self, codAsociado):
        encontrado = False
        i = 0
        nomFacultad = None
        while not encontrado and i < self.__cantidad:
            if self.__listaF[i].getCodigoFacultad() == codAsociado:
                encontrado = True
                nomFacultad = self.__listaF[i].getNombreFacultad()
            else:
                i += 1
        return nomFacultad
    
    # Inciso D
    def calcularTotalCarreras(self, manejadorC):
        for i in range(self.__cantidad):
            cont = 0
            codF = self.__listaF[i].getCodigoFacultad()
            for j in range(manejadorC.totalCarreras()):
                if manejadorC.getCodigoFacultadPorCarreraIndice(j) == codF:
                    cont += 1
            print(f"En la facultad {self.__listaF[i].getNombreFacultad()} se dictan {cont} carreras.")
            #j = 0 Innecesario, se reinicia en el siguiente bucle al cambiar de facultad

    # Inciso E
    def listarCarreras(self, nomFacultad, manejadorC):
        i = 0
        encontrado = False
        while not encontrado and i < self.__cantidad:
            if self.__listaF[i].getNombreFacultad() == nomFacultad:
                manejadorC.ordenarCarreras()
                encontrado = True
            else:
                i += 1
        
        if encontrado:
            print(f"\nListado de carreras que se dictan en {nomFacultad}:")
            for j in range(manejadorC.totalCarreras()):
                if manejadorC.getCodigoFacultadPorCarreraIndice(j) == self.__listaF[i].getCodigoFacultad():
                    manejadorC.printCarrera(j)
        else:
            print(f"\nNo se encontró la {nomFacultad}.")
