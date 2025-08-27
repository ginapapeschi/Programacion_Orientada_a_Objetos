from gestorMedios import Lista

def menu():
    print()
    print("MENÚ DE OPCIONES".center(70))
    op = int(input('''
1) Insertar medios a la colección en una posición específica
2) Agregar medios a la colección
3) Mostrar medios almacenados en la colección
4) Mostrar información donde se transmite un programa de Televisión
5) Listar información de una emisora
6) Cantidad de diarios y revistas almacenadas en la colección
0) SALIR
                                                                         
Su opción --> '''))
    return op

if __name__ == '__main__':
    gestor = Lista()
    gestor.cargarCSVMediosYProgramas()
    opcion = menu()

    while opcion != 0:
        
        if opcion == 1:
            try:
                posicion = int(input("\nIngrese la posición donde desea insertar el medio: "))
                gestor.agregarMedioPorPosicion(posicion)
            except IndexError as i:
                print(i)

        elif opcion == 2:
            try:
                gestor.agregarManual()
            except TypeError as t:
                print(t)

        elif opcion == 3:
            gestor.mostrarMedios()

        elif opcion == 4:
            nomPrograma = input("\nIngrese el nombre del programa: ")
            gestor.inciso4(nomPrograma)

        elif opcion == 5:
            nomEmisora = input("\nIngrese el nombre de la emisora: ")
            gestor.inciso5(nomEmisora)

        elif opcion == 6:
            gestor.inciso6()

        else:
            print("\nERROR - Opción inválida.")
        
        opcion = menu()
    
    print("\nPrograma finalizado.")