from gestorClientes import GestorCliente
from gestorMovimientos import GestorMovimiento

def menu_opciones():
    op = str(input("""
                                                    MENÚ DE OPCIONES
        a) Ingrese el DNI del cliente para actualizar saldo.
        b) Ingrese número de tarjeta del cliente para informar nombre y apellido si no hubo movimientos en abril de 2024.
        c) Ordenar gestor de movimientos por número de tarjeta.
        d) Salir del menú.
        Su opción --> """))
    return(op.lower())


if __name__ == "__main__":
    gestorCliente = GestorCliente()
    gestorMovimiento = GestorMovimiento()
    gestorCliente.leerCSV()
    gestorMovimiento.leerCSV()
    opcion = menu_opciones()

    while opcion != "d":

        if opcion == "a":
            dniIngresado = int(input("\nIngrese DNI del cliente: "))
            gestorCliente.actualizarSaldo(dniIngresado, gestorMovimiento)

        elif opcion == "b":
            numTarjetaIngresado = int(input("\nIngrese número de tarjeta del cliente: "))
            gestorMovimiento.movimientosAbril(numTarjetaIngresado, gestorCliente)

        elif opcion == "c":
            gestorMovimiento.ordenarPorNroTarjeta()
            opcion = menu_opciones()

        else:
            print("\nERROR - Opción inválida")
            opcion = menu_opciones()

    opcion = menu_opciones()
