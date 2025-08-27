from gestorHoteles import GestorHotel

def menu():
    print()
    print("MENÚ DE OPCIONES".center(70))
    op = int(input('''
1) Agregar habitaciones al hotel
2) Reservar habitación
3) Liberar habitación
4) Mostrar número y piso de las habitaciones de un tipo
5) Mostrar cantidad de habitaciones libres por piso
6) Mostrar listado de habitaciones
0) SALIR         
          
Su opción --> '''))
    
    return op

if __name__ == '__main__':
    gestorHotel = GestorHotel()
    gestorHotel.cargarCSVHoteles()
    opcion = menu()
    
    while opcion != 0:
        if opcion == 1:
            nomHotel = input("\nIngrese el nombre del hotel: ")
            gestorHotel.agregarHabitacionManual(nomHotel)
            
        elif opcion == 2:
            nomHotel = input("\nIngrese el nombre del hotel: ")
            gestorHotel.reservarHabitacion(nomHotel)

        elif opcion == 3:
            nomHotel = input("\nIngrese el nombre del hotel: ")
            gestorHotel.liberarHabitacion(nomHotel)
        
        elif opcion == 4:
            tipoHab = input("\nIngrese el tipo de habitación: ")
            gestorHotel.infoTipoHabitacion(tipoHab)
        
        elif opcion == 5:
            gestorHotel.mostrarHabitacionesLibres()

        elif opcion == 6:
            gestorHotel.mostrarListado()

        else:
            print("ERROR - Opción inválida.")
        
        opcion = menu()