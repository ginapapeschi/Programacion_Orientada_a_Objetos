from claseControl import Control

def menu():
    print()
    print("MENÚ DE OPCIONES".center(70))
    op = input('''
a) Agregar medios de comunicación
b) Mostrar información de un programa
c) Mostrar medios
z) SALIR
Su opción --> ''')
    return op

if __name__ == '__main__':
    gestor = Control()
    try:
        gestor.cargarCSV()
    except ValueError as ve:
        print(ve)

    opcion = menu().lower()

    while opcion != 'z':
        if opcion == 'a':
            tipoMedio = input("\nIngrese el tipo de medio (Radio/Prensa): ")
            gestor.agregarManual(tipoMedio)

        elif opcion == 'b':
            try:
                nomPrograma = input("\nIngrese el nombre del programa: ")
                gestor.incisoB(nomPrograma)
            except ValueError as v:
                print(v)

        elif opcion == 'c':
            gestor.mostrarMedios()

        else:
            print("\nERROR - Opción no válida")

        opcion = menu().lower()

    print("\nPrograma finalizado")