class Biblioteca:
    __nombre: str
    __direccion: str
    __telefono: str
    __listaLibros: list

    def __init__(self, nom, dir, tel):
        self.__nombre = nom
        self.__direccion = dir
        self.__telefono = tel
        self.__listaLibros = []

    def agregarLibro(self, unLibro):                                # Se recibe la parte ya creada como PARÁMETRO.
        self.__listaLibros.append(unLibro)
        print("Libro cargado.")

    def getNombre(self):
        return self.__nombre
    
    def getDireccion(self):
        return self.__direccion
    
    def getTelefono(self):
        return self.__telefono
    
    # Inciso b
    def eliminarLibroPorISBN(self, isbn):
        encontrado = False
        i = 0
        while not encontrado and i < len(self.__listaLibros):
            if self.__listaLibros[i].getISBN() == isbn:
                encontrado = True
                del self.__listaLibros[i]
                return                                              # Para que no siga iterando.
            
            else:
                i += 1
        
        raise IndexError("ERROR - No se encontró el libro con el ISBN ingresado.")

    # Inciso c
    def buscarLibroPorTitulo(self, titulo):
        i = 0
        while i < len(self.__listaLibros):
            if self.__listaLibros[i].getTitulo().lower() == titulo.lower():
                return self.__listaLibros[i]
            
            else:
                i += 1

    # Inciso d
    def mostrarLibros(self, nomBiblio):
        print()
        print(f"--- Libros de la {nomBiblio} ---".center(45))
        for libro in self.__listaLibros:
            print(f"- {libro.getTitulo()}")
