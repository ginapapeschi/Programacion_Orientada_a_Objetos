from gestorMamas import GestorMama
from gestorNacimientos import GestorNacimiento

def menu():
    print()
    print("MENÚ DE OPCIONES".center(60))
    op = input("""
(a) Ingresar el DNI de una mamá para mostrar su información
(b) Mostrar datos de la/s mamá/s que han tenido parto múltiple
(c) SALIR
Su opción --> """)
    
    return op

if __name__ == '__main__':
    gestorMama = GestorMama()
    gestorNac = GestorNacimiento()
    gestorMama.cargarCSVMamas()
    gestorNac.cargarCSVNacimientos()
    opcion = menu().lower()
    
    while opcion != 'c':
        if opcion == 'a':
            dniMama = input("\nIngrese el DNI de la mamá: ")
            gestorMama.mostrarInfoMama(dniMama, gestorNac)
        
        elif opcion == 'b':
            pass
        
        else:
            print("ERROR - Opción inválida.")

        opcion = menu().lower()