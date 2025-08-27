from ClaseNodo import Nodo
from ClaseHerramientas import Herramienta
from ClaseMaquinaria import Maquinaria
from ClaseEquipo import Equipo
import csv

class Lista:
    __comienzo: Nodo
    __actual: Nodo
    __indice: int
    __tope: int

    def __init__(self):
        self.__comienzo = None
        self.__actual = None
        self.__tope = 0
        self.__indice = 0 

    def __iter__(self):
        return self 
    
    def __getTope(self):
        return self.__tope

    def __next__(self):
        if self.__indice == self.__tope: 
            self.__actual = self.__comienzo
            self.__indice = 0 
            raise StopIteration 
        else:  
            self.__indice += 1  
            dato = self.__actual.getDato()
            self.__actual = self.__actual.getSiguiente() 
            return dato 
        
    def agregarEquipo(self, eq):
        nodo = Nodo(eq)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo = nodo
        self.__actual = nodo
        self.__tope += 1
        
    def cargarEquipo(self):
        band1 = False
        band2 = False
        archivo = open("equipos.csv")
        reader = csv.reader(archivo, delimiter = ";")
        next(reader)
        for fila in reader:
            if fila[0] == "M":
                maquinaria = (Maquinaria(fila[1], fila[2], int(fila[3]), fila[4], fila[5], fila[6], int(fila[7]), int(fila[8]), fila[9], int(fila[10])))
                self.agregarEquipo(maquinaria)
                print("Maquinaria cargada exitosamente.")
                band1 = True
            elif fila[0] == "E":
                herramienta = (Herramienta(fila[1], fila[2], int(fila[3]), fila[4], fila[5], fila[6], int(fila[7]), int(fila[8]), fila[9]))
                self.agregarEquipo(herramienta)
                print("Herramienta cargada exitosamente.")
                band2 = True
        if band1 and band2:
            print("\nArchivo cargado exitosamente.")
        archivo.close()

    def mostrarEquipoPos(self, pos):
        if pos < self.__getTope():
            aux = self.__comienzo
            for i in range(pos):
                aux = aux.getSiguiente()
            if isinstance(aux.getDato(), Herramienta):
                print(f"El tipo de equipo en la posición {pos + 1} es del tipo Herramienta.")
            elif isinstance(aux.getDato(), Maquinaria):
                print(f"El tipo de equipo en la posición {pos + 1} es del tipo Maquinaria.")
        else:
            raise IndexError("\nERROR - Índice fuera de rango.")

    def mostrarCantHerramientasFabricadas(self, anio):
        cont = 0
        aux = self.__comienzo
        while aux is not None:
            if isinstance(aux.getDato(), Herramienta) and aux.getDato().getAnio() == anio:
                cont += 1
            aux = aux.getSiguiente()
        print(f"Hay {cont} herramientas eléctricas fabricadas en el año {anio}.")
        
    def mostrarCantMaquinariasCapacidad(self, capacidad):
        cont = 0
        aux = self.__comienzo
        while aux is not None:
            if isinstance(aux.getDato(), Maquinaria):
                if int(aux.getDato().getCapacidadCarga()) <= capacidad:
                    cont += 1
            aux = aux.getSiguiente()
        if cont == 1:
            print(f"Hay {cont} maquinaria capaz de cargar {capacidad} toneladas.")
        elif cont != 0:
            print(f"Hay {cont} maquinarias capaces de cargar {capacidad} toneladas.")
    
    def mostrarEquipos(self):        
        aux = self.__comienzo
        for aux in self:
            print("")
            print(aux)
            print(f"Tarifa de alquiler: ${aux.calcularTarifaAlquiler():.2f}")
