from gestorDepto import GestorDepto
from claseAccidente import Accidente

def menu():
    print()
    print("MENÚ DE OPCIONES".center(100))
    op = (input('''CARGA - Cargar accidentes del año anterior                
a) Mostrar departamentos y accidentes por mes ingresado
b) Obtener departamento con la mayor cantidad de accidentes en el mes ingresado
c) Indicar la cantidad total de accidentes ocurridos el año anterior en el departamento ingresado
d) Mostrar total de datos registrados
z) SALIR                                         

Su opción ---> '''))
    return op

if __name__ == '__main__':
    gestorD = GestorDepto()
    tablaAccidentes = Accidente()
    tablaAccidentes.cerear()
    gestorD.cargarDeptos()
    opcion = menu().lower()

    while opcion != 'z':

        if opcion == 'carga':
            depto = int(input("\nIngrese el número del departamento (1-19): "))
            mes = int(input("Ingrese el número del mes (1-12): "))
            cantAccidentes = int(input("Ingrese la cantidad de accidentes: "))
            tablaAccidentes.cargarTabla(depto, mes, cantAccidentes)

        elif opcion == 'a':
            mes = int(input("\nIngrese el número del mes (1-12): "))
            gestorD.incisoA(mes, tablaAccidentes)

        elif opcion == 'b':
            mes = int(input("\nIngrese el número del mes (1-12): "))
            gestorD.incisoB(mes, tablaAccidentes)

        elif opcion == 'c':
            nomDepto = (input("\nIngrese el nombre del departamento: "))
            gestorD.incisoC(nomDepto, tablaAccidentes)
    
        elif opcion == 'd':
            gestorD.incisoD(tablaAccidentes)

        else:
            print("\nERROR - Opción no válida.")

        opcion = menu()