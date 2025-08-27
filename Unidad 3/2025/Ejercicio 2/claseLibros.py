class Libro:
    __titulo: str
    __autor: str
    __isbn: str
    __genero: str

    def __init__(self, titulo, autor, isbn, gen):
        self.__titulo = titulo
        self.__autor = autor
        self.__isbn = isbn
        self.__genero = gen

    def __del__(self):
        print(f"Libro '{self.__titulo}' eliminado exitosamente.")

    def getTitulo(self):
        return self.__titulo
    
    def getAutor(self):
        return self.__autor
    
    def getISBN(self):
        return self.__isbn
    
    def getGenero(self):
        return self.__genero