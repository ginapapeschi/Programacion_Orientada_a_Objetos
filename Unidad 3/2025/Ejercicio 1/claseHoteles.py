import csv
from claseHabitaciones import Habitacion

class Hotel:
    __nombre: str
    __direccion: str
    __telefono: str
    __listaHab: list

    def __init__(self, nom, dir, tel):
        self.__nombre = nom
        self.__direccion = dir
        self.__telefono = tel
        self.__listaHab = []    

    def getNombre(self):
        return self.__nombre
    
    def getDireccion(self):
        return self.__direccion
    
    def getTelefono(self):
        return self.__telefono    
    
    # Inciso 1)
    def agregarHabitacion(self, num, piso, tipo, precio, disp):         # La clase contenedora CREA la parte, no la recibe ya creada como parámetro.
        habitacion = Habitacion(num, piso, tipo, precio, disp)
        self.__listaHab.append(habitacion)
        print("Habitación cargada.")

    # Inciso 2) y 3)                                                    # Me dio paja y reutilicé código ahre
    def buscarHabitacion(self, numHabitacion, opcion):
        encontrado = False
        i = 0
        while not encontrado and i < len(self.__listaHab):
            if self.__listaHab[i].getNumero() == numHabitacion:
                encontrado = True
                disponible = self.__listaHab[i].getDisponibilidad()

                if opcion == 1 and disponible:                          # Si se reserva la habitación.
                    self.__listaHab[i].setDisponibilidad(False)
                    print("\nHabitación reservada exitosamente.")

                elif opcion == 1 and not disponible:
                    print(f"\nERROR - La habitación {numHabitacion} no está disponible.")
                
                elif opcion == 2 and not disponible:                    # Si se libera la habitación.
                    self.__listaHab[i].setDisponibilidad(True)
                    print("\nHabitación liberada exitosamente.")
                
                elif opcion == 2 and disponible:
                    print(f"\nERROR - La habitación {numHabitacion} ya se encontraba libre.")
            
            else:
                i += 1
        
        if not encontrado:
            print("\nERROR - La habitación ingresada no existe.")
    
    # Inciso 4)
    def mostrarNumeroYPiso(self, tipo, nomHotel):
        encontrado = False
        encabezado = False
        for habitacion in self.__listaHab:
            if habitacion.getTipo().lower() == tipo.lower():
                encontrado = True
                if not encabezado:
                    print()
                    print(f"--- {tipo.capitalize()}s - {nomHotel} ---".center(40))
                    encabezado = True
                print(f"Habitación {habitacion.getNumero()} - Piso {habitacion.getPiso()}")
        
        return encontrado

    # Inciso 5)
    def mostrarCantLibresPorPiso(self, nomHotel):
        print()
        print(f"--- {nomHotel} ---".center(40))

        for piso in range(1, 5):
            cont = 0
            for habitacion in self.__listaHab:
                if habitacion.getPiso() == piso and habitacion.getDisponibilidad() is True:
                    cont += 1
                
            if cont > 1:
                print(f"Piso {piso} - {cont} habitaciones libres")

            elif cont == 1:
                print(f"Piso {piso} - 1 habitación libre")

    # Inciso 6)
    def listarHabitaciones(self, nomHotel):
        print()
        print(f"--- {nomHotel} ---".center(45))

        for tipo in ['sencilla', 'doble', 'suite']:
            print(f"\n- Tipo de habitación: {tipo}")
            print(f"{'Número':<6} | {'Piso':<4} | {'Precio por noche':<15} | {'Disponibilidad':<20}")

            for habitacion in self.__listaHab:
                if habitacion.getTipo().lower() == tipo.lower():
                    print(f"{habitacion.getNumero():<6} | {habitacion.getPiso():<4} | ${habitacion.getPrecio():<15.2f} | ", end='')
                    if habitacion.getDisponibilidad() is True:
                        print(f"{'Libre':<20}")
                    else:
                        print(f"{'Reservado':<20}")
