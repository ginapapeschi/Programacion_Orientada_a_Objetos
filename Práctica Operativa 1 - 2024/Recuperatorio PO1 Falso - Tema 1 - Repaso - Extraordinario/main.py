from gestorCabanas import GestorCabana
from gestorReservas import GestorReserva

def menu_opciones():
    op = str(input("""
                                                        MENÚ DE OPCIONES
a) Ingresar cantidad de huéspedes y mostrar número de cabañas con capacidad igual o mayor a la ingresada y que NO tienen reserva registrada
b) Ingresar fecha y emitir listado con las reservas cuya FECHA DE INICIO del hospedaje sea IGUAL a la ingresada.
c) SALIR
Su opción --> """))
    
    return (op.lower())

if __name__ == "__main__":
    gestorCabana = GestorCabana()
    gestorReserva = GestorReserva()
    gestorCabana.leerCSVCabana()
    gestorReserva.leerCSVReserva()
    opcion = menu_opciones()

    while opcion != "c":
        if opcion == "a":
            cantHuespedes = int(input("\nIngresar cantidad de huéspedes: "))
            gestorCabana.mostrarCabanaCapacidad(cantHuespedes, gestorReserva)

        elif opcion == "b":
            fecha = (input("\nIngresar fecha con el formato dd/mm/aa: "))
            gestorReserva.listadoReservados(fecha, gestorCabana)

        else:
            print("\nERROR - Opción inválida")
            opcion = menu_opciones

        opcion = menu_opciones()

