from claseControlRutas import GestorRuta
from claseControlVehículos import GestorVehiculo

def menu():
    print()
    print("MENÚ DE OPCIONES".center(70))
    op = input('''
a) Agregar vehículos
b) Mostrar rutas asociadas a un vehículo
c) Mostrar vehículos
d) SALIR
Su opción --> ''')
    return op

if __name__ == '__main__':
    gestorRuta = GestorRuta()
    gestorVehiculo = GestorVehiculo()
    gestorRuta.cargaCSVRutas()
    opcion = menu().lower()

    while opcion != 'd':
        if opcion == 'a':
            tipoVehiculo = input("\nIngrese el tipo de vehículo (Automóvil/Camión): ")
            gestorVehiculo.agregarVehiculo(tipoVehiculo, gestorRuta)
        
        elif opcion == 'b':
            try:
                matricula = input("\nIngrese la matrícula: ")
                gestorVehiculo.incisoB(matricula)
            except Exception as e:
                print(e)

        elif opcion == 'c':
            gestorVehiculo.mostrarVehiculos()

        else:
            print("\nERROR - Opción no válida")

        opcion = menu().lower()

    print("\nPrograma finalizado")