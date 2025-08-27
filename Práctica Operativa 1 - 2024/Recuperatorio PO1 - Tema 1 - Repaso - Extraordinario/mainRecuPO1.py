from gestorMamas import gestorMama
from gestorNacimientos import gestorNacimiento

def menu_opciones():
    op = str(input("""
                                    MENÚ DE OPCIONES
            a) Ingresar por teclado el DNI de una mamá para mostrar su información.
            b) Mostrar datos de la/s mamá/s que han tenido parto múltiple.
            c) Salir.
            Su opción --> """))
    return (op.lower())

if __name__ == "__main__":
    gestorMama = gestorMama()
    gestorNacimiento = gestorNacimiento()
    gestorMama.leerCSV()
    gestorNacimiento.leerCSV()
    opcion = menu_opciones()

    while opcion != "c":

        if opcion == "a":
            dniMama = int(input("\nIngrese el DNI: "))
            gestorMama.buscarDNI(dniMama, gestorNacimiento)
        
        elif opcion == "b":
            gestorNacimiento.mostrarDatosPartoMultiple(gestorMama)
            pass

        opcion = menu_opciones() 
