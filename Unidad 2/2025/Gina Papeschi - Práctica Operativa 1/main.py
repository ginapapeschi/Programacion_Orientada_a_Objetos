# Nombre: Papeschi Gina
# DNI: 46407532
# Número de registro: E010-252

from gestorGastos import GestorGasto
from gestorMovilidades import GestorMovilidad

def menu():
    print()
    print("MENÚ DE OPCIONES".center(70))
    op = input('''
a) Listar gastos en el mes de abril
b) Informar los gastos del cliente durante la fecha ingresada
c) Ordenar gastos y listar movilidades por fecha                                            
d) SALIR

Su opción --> ''')
    
    return op

if __name__ == '__main__':
    gestorGastos = GestorGasto()
    gestorMov = GestorMovilidad()
    gestorGastos.cargarCSVGastos()
    gestorMov.cargarCSVMovilidades()
    opcion = menu().lower()

    while opcion != 'd':
        if opcion == 'a':
            patente = input("\nIngrese la patente: ")
            gestorMov.listarMovilidades(patente, gestorGastos)
            
        elif opcion == 'b':
            fecha = input("\nIngrese la fecha: ")
            gestorGastos.gastosEnElDia(fecha)
            
        elif opcion == 'c':
            fecha = input("\nIngrese la fecha: ")
            gestorMov.incisoC(fecha, gestorGastos)

        else:
            print("\nERROR - Opción inválida.")
        
        opcion = menu().lower()