from claseLista import Lista
from claseVehiculo import Vehiculo

def menu():
    print()
    print("MENÚ DE OPCIONES".center(75))
    op = int(input('''
1) Cargar vehículos y baterías
2) Listar patentes que pueden recorrer una distancia con la energía disponible
3) Mostrar información de vehículos
4) Agregar un colectivo en una posición de la lista
0) SALIR
Su opción --> '''))
    return op

if __name__ == '__main__':
    gestor = Lista()
    opcion = menu()

    while opcion != 0:
        if opcion == 1:
            print()
            gestor.cargarCSV()

        elif opcion == 2:
            print()
            distancia = float(input("Ingrese distancia a recorrer en km: "))
            gestor.listarPatentes(distancia)

        elif opcion == 3:
            gestor.mostrarVehiculos()

        elif opcion == 4:
            try:
                print()
                posicion = int(input("Ingrese la posición: "))
                gestor.agregarManual(posicion)
            except IndexError as ie:
                print(ie)

        else:
            print("ERROR - Opción inválida")

        opcion = menu()
    
    print()
    print("Programa finalizado")