from gestorBiblioteca import GestorBiblioteca

def menu():
    print()
    print("MENÚ DE OPCIONES".center(70))
    op = input('''
a) Agregar libro
b) Eliminar libro
c) Mostrar información de un libro
d) Listar libros
z) SALIR
                                                                         
Su opción --> ''')
    return op

if __name__ == '__main__':
    gestorBiblio = GestorBiblioteca()
    gestorBiblio.cargarCSVBibliotecas()
    opcion = menu().lower()

    while opcion != 'z':
        try:
            if opcion == 'a':
                nomBiblio = input("\nIngrese el nombre de la biblioteca: ")
                gestorBiblio.agregarLibrosManual(nomBiblio)

            elif opcion == 'b':
                nomBiblio = input("\nIngrese el nombre de la biblioteca: ")
                isbn = input("Ingrese el ISBN del libro: ")
                gestorBiblio.eliminarLibro(nomBiblio, isbn)

            elif opcion == 'c':
                titulo = input("\nIngrese el título del libro: ")
                gestorBiblio.mostrarInfoLibro(titulo)

            elif opcion == 'd':
                gestorBiblio.listarLibros()

            else:
                print("\nERROR - Opción inválida.")

        except IndexError as e:
            print(e)

        opcion = menu().lower()