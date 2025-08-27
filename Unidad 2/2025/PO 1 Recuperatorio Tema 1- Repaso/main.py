from gestorCabañas import GestorCabaña
from gestorReservas import GestorReserva

def menu():
    print()
    print("MENU DE OPCIONES".center(60))
    op = input('''
a) Mostrar número de cabaña con capacidad igual o mayor a la cantidad de huéspedes ingresada y sin reserva registrada
b) Emitir listado de reservas               
c) SALIR
Su opción --> ''')
    
    return op

if __name__ == '__main__':
    gestorCab = GestorCabaña()
    gestorRes = GestorReserva()
    gestorCab.cargarCSVCabañas()
    gestorRes.cargarCSVReservas()
    opcion = menu().lower()

    while opcion != 'c':
        if opcion == 'a':
            cantH = int(input("\nIngrese la cantidad de huéspedes: "))
            gestorCab.cabañasSinReserva(cantH, gestorRes)

        elif opcion == 'b':
            fecha = input("\nIngrese la fecha (formato dd/mm/aa): ")
            gestorRes.listadoReservasFecha(fecha, gestorCab)
            
        else:
            print("\nERROR - Opción inválida.")

        opcion = menu().lower()