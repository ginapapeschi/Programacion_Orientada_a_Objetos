from GestorEdificios import GestorEdificio

def menu_opciones():
    op = None
    try:
        op = int(input('''
                                                ------MENÚ DE OPCIONES------
                       
    (1) Ingresar nombre de edificio para mostrar nombre y apellido del propietario de cada departamento.
    (2) Mostrar superficie total cubierta de un edificio.
    (3) Ingresar el nombre de un propietario para mostrar la superficie total cubierta de su departamento.
    (4) Ingresar el número de piso para mostrar la cantidad de departamentos que tienen 3 dormitorios y más de un baño.
    (0) SALIR DEL MENÚ
    Su opción --> '''))
    except ValueError:      # Ver esto
        pass
    return op

if __name__ == '__main__':
    GEdi = GestorEdificio()
    GEdi.cargaEdificio()
    opcion = menu_opciones()
    while opcion != 0:
        if opcion == 1:
            try:
                print(" ")
                op1 = (input("Ingrese el nombre del edificio (Edificio Norte/Edificio Sur): "))
                op1 = op1.title()   # el método .title() sirve para capitalizar (convertir en mayúsculas) la PRIMERA LETRA de cada palabra.
                GEdi.mostrarPropietarios(op1)
            except AssertionError:
                print("ERROR - No existe un edificio con el nombre ingresado.") # Para que funcione el except, debe haber un "assert" en el método al que se ingresa, de este modo comprueba el error.

        elif opcion == 2:
            try:
                print(" ")
                op2 = int(input("Ingrese el ID de un edificio (1-2): "))
                GEdi.mostrarSuperficieEdificio(op2)
            except AssertionError:
                print("ERROR - No existe un edificio con el ID ingresado.")
        
        elif opcion == 3:
            try:
                print(" ")
                op3 = (input("Ingrese el nombre del propietario: "))
                op3 = op3.title()
                GEdi.mostrarSuperficieDepto(op3)
            except AssertionError:
                print("ERROR - No existe un propietario con el nombre ingresado.")
        
        elif opcion == 4:
            try:
                print("\n")
                op4 = int(input("Ingrese el número de piso: "))
                GEdi.mostrarCantDeptosCondiciones(op4)
            except ValueError:
                print("ERROR - Ingrese un número entero.")
            except AssertionError:
                print("ERROR - No existe el número de piso ingresado.")
        else:
            print('''   
                                                ------OPCIÓN INVÁLIDA------''')
        opcion = menu_opciones()