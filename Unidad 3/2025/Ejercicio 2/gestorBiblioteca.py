import csv
from claseBibliotecas import Biblioteca
from claseLibros import Libro

class GestorBiblioteca:
    __listaBiblio: list

    def __init__(self):
        self.__listaBiblio = []

    def agregarBiblioteca(self, unaBiblio):
        self.__listaBiblio.append(unaBiblio)
        print("Biblioteca cargada.")

    def cargarCSVBibliotecas(self):
        biblio = None
        archivo = open('Biblioteca.csv', encoding='utf-8')
        reader = csv.reader(archivo, delimiter=';')
        for fila in reader:
            if len(fila) == 3:
                biblio = Biblioteca(fila[0], fila[1], fila[2])
                self.agregarBiblioteca(biblio)

            elif len(fila) == 4 and biblio is not None:
                libro = Libro(fila[0], fila[1], fila[2], fila[3])   # En la agregación se crea un libro en el gestor, no en la clase Biblioteca (el todo, a diferencia de la composición).
                biblio.agregarLibro(libro)
                
        archivo.close()

    # Búsqueda de Biblioteca
    def buscarBiblioteca(self, nomBiblio):
        i = 0
        while i < len(self.__listaBiblio):
            if self.__listaBiblio[i].getNombre().lower() == nomBiblio.lower():
                return self.__listaBiblio[i]

            else:
                i += 1
    
        print("\nERROR - No se encontró la biblioteca ingresada")
            

    # Inciso a
    def agregarLibrosManual(self, nomBiblio):
        biblio = self.buscarBiblioteca(nomBiblio)
        if biblio:
            titulo = input("Ingrese el título del libro: ")
            autor = input("Ingrese el autor: ")
            isbn = input("Ingrese el ISBN: ")
            genero = input("Ingrese el género: ")
            unLibro = Libro(titulo, autor, isbn, genero)
            biblio.agregarLibro(unLibro)

    # Inciso b
    def eliminarLibro(self, nomBiblio, isbn):
        biblio = self.buscarBiblioteca(nomBiblio)
        if biblio:
            biblio.eliminarLibroPorISBN(isbn)

    # Inciso c
    def mostrarInfoLibro(self, titulo):
        encontrado = False
        encabezado = False
        for biblio in self.__listaBiblio:                           # Con for en caso de que más de una biblioteca tenga el mismo libro
            libro = biblio.buscarLibroPorTitulo(titulo)
            if libro:
                if not encabezado:
                    print()
                    print(f"--- Información de '{libro.getTitulo()}' ---".center(55))
                    encabezado = True
                print(f"- Biblioteca en la que se encuentra: {biblio.getNombre()}")
                print(f"- Autor: {libro.getAutor()}")
                print(f"- Género: {libro.getGenero()}")
                encontrado = True

        if not encontrado:
            print("\nERROR - No se encontró el libro con el título ingresado.")

    # Inciso d
    def listarLibros(self):
        for biblio in self.__listaBiblio:
            biblio.mostrarLibros(biblio.getNombre())