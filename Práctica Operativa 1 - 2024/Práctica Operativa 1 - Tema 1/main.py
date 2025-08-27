from GestorCliente import GestorCli
from GestorMovimiento import GestorMov

def menu_opciones():
    op = str(input("""
                                            MENÚ DE OPCIONES
        a) Ingrese el DNI del cliente para actualizar saldo.
        b) Ingrese número de tarjeta del cliente para informar nombre y apellido si no hubo movimientos en abril de 2024.
        c) Ordenar por número de tarjeta.
        d) Salir del menú.
        Su opción --> """))
    return(op)

if __name__ == '__main__':
    GMov = GestorMov()
    GCli = GestorCli()
    GMov.leerdatos()
    GCli.leerdatos()
    opcion = menu_opciones()
    while opcion != 'd':
        if opcion == 'a':
            GCli.actualizarSaldo(GMov)
        elif opcion == 'b':
            GMov.buscaTarjeta(GCli)
        elif opcion == 'c':
            GMov.ordenarMov()
            GMov.listarMov()
        opcion = menu_opciones()
        

