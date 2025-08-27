from ClaseNodo import Nodo
from ClaseAudioLibro import AudioLibro
from ClaseLibroImpreso import LibroImpreso
import csv

class Lista:
    __comienzo: Nodo
    __actual: Nodo
    __indice: int
    __tope: int

    def __init__ (self):
        self.__comienzo = None
        self.__actual = None
        self.__indice = 0
        self.__tope = 0

    def __iter__ (self):
        return self
    
    def __next__ (self):
        if self.__indice == self.__tope:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            self.__indice += 1
            dato = self.__actual.getDato()
            self.__actual = self.__actual.getSiguiente()
            return dato
        
    def getTope(self):
        return self.__tope

######

    def agregarPublicacion(self, publicacion):
        nodo = Nodo(publicacion)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo = nodo
        self.__actual = nodo
        self.__tope += 1
        print("Cargado Exitosamente")

    def cargarPublicaciones(self):
        band1 = False
        band2 = False
        archivo1 = open("libros.csv")
        reader1 = csv.reader(archivo1,delimiter=";")
        for fila1 in reader1:
            if band1 is False:
                band1 = True
            else:
                self.agregarPublicacion(LibroImpreso(tit = fila1[0], cate = fila1[1], precioB = float(fila1[2]), nomAutor = fila1[3], fechaEdi = fila1[4], cantPag = int(fila1[5])))
        archivo1.close()
        archivo2 = open("cd.csv")
        reader2 = csv.reader(archivo2, delimiter = ";")
        for fila2 in reader2:
            if band2 is False:
                band2 = True
            else:
                self.agregarPublicacion(AudioLibro(tit = fila2[0], cate = fila2[1], precioB = float(fila2[2]), tiempoRep = int(fila2[3]), nomNarra = fila2[4]))
        archivo2.close()