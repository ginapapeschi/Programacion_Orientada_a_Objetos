from gestorBiblioteca import GestorBiblioteca
from claseBibliotecas import Biblioteca

def test():
    gestorBiblio = GestorBiblioteca()
    respuesta = input("\n¿Desea cargar datos? Respuesta (Sí/No): ")
    while respuesta.lower() != 'no':
        if respuesta.lower() == 'sí':
            op = input("Elija una opción (Biblioteca/Libro): ")
            if op.lower() == 'biblioteca':
                print("Ingrese la información necesaria:")
                nombreBiblioteca = input("Nombre de la biblioteca: ")
                dir = input("Dirección: ")
                tel = input("Teléfono: ")
                biblioteca = Biblioteca(nombreBiblioteca, dir, tel)
                gestorBiblio.agregarBiblioteca(biblioteca)

            elif op.lower() == 'libro':
                nomBiblioteca = input("Ingrese el nombre de la biblioteca: ")
                gestorBiblio.agregarLibrosManual(nomBiblioteca)

        else:
            print("\nERROR - Opción inválida")

        respuesta = input("\n¿Desea cargar datos? Respuesta (Sí/No): ")

if __name__ == '__main__':
    test()
    
    