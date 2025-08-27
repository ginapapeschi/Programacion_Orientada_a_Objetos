from gestorPlanes import GestorPlanes

def menu():
    op = None
    print()
    print("MENÚ DE OPCIONES".center(75))
    try:
        op = int(input('''
1) Mostrar plan almacenado en una posición
2) Mostrar cantidad de planes que tiene una cobertura geográfica
3) Mostrar el/los nombres de compañías que ofrecen la cantidad de canales ingresada
4) Mostrar planes
0) SALIR
Su opción --> '''))
    except ValueError:
        print("\nERROR - Se espera un entero.")
    return op

if __name__ == '__main__':
    gestor = GestorPlanes()
    gestor.cargarCSVPlanes()
    opcion = menu()

    while opcion != 0:
        if opcion == 1:
            try:
                posicion = int(input("\nIngrese la posición: "))
                gestor.mostrarPlanPorPosicion(posicion)
            except IndexError as i:
                print(i)

        elif opcion == 2:
            cobertura = input("\nIngrese la cobertura: ")
            gestor.mostrarPlanesPorCobertura(cobertura)

        elif opcion == 3:
            cantCanales = int(input("\nIngrese la cantidad de canales internacionales: "))
            gestor.mostrarCompaniasPorCantidad(cantCanales)

        elif opcion == 4:
            gestor.mostrarPlanes()

        elif opcion != None:
            print("\nERROR - Opción no válida.")

        opcion = menu()

    print("Programa finalizado.")