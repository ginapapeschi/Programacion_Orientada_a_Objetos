from gestorClientes import GestorClientes
from gestorMovimientos import GestorMovimientos

def menu():
    print()
    print("MENÚ DE OPCIONES".center(60))
    op = input('''
a) Actualizar saldo y armar listado
b) Informar si el cliente no tuvo movimientos durante el mes de abril
c) Ordenar movimientos                                             
d) SALIR

Su opción --> ''')
    
    return op

if __name__ == '__main__':
    gestorCli = GestorClientes()
    gestorMov = GestorMovimientos()
    gestorCli.cargarCSVClientes()
    gestorMov.cargarCSVMov()
    opcion = menu().lower()

    while opcion != 'd':
        if opcion == 'a':
            dni = input("\nIngrese el DNI: ")
            gestorCli.actualizarSaldo(dni, gestorMov)

        elif opcion == 'b':
            numTarjeta = int(input("\nIngrese el número de tarjeta: "))
            gestorCli.mostrarSiTuvoMovimientos(numTarjeta, gestorMov)

        elif opcion == 'c':
            gestorMov.ordenarMovimientos()

        else:
            print("\nERROR - Opción inválida.")
        
        opcion = menu().lower()