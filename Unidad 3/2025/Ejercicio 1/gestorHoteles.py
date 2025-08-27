import csv
from claseHoteles import Hotel

class GestorHotel:
    __listaHoteles: list

    def __init__(self):
        self.__listaHoteles = []

    def agregarHotel(self, unHotel):
        self.__listaHoteles.append(unHotel)
        print("Hotel cargado.")

    def cargarCSVHoteles(self):
        archivo = open('Hoteles.csv', encoding='utf-8')
        reader = csv.reader(archivo, delimiter=';')
        for fila in reader:
            if len(fila) == 3:                          # Detecta si tiene 3 columnas, es un hotel.
                hotel = Hotel(fila[0], fila[1], fila[2])
                self.agregarHotel(hotel)
            elif len(fila) == 5 and hotel is not None:  # Detecta si es una habitación y que el hotel esté cargado.
                num = int(fila[0])
                piso = int(fila[1])
                tipo = fila[2]
                precio = float(fila[3])
                if fila[4].lower() == "true":
                    disp = True
                else:
                    disp = False
                hotel.agregarHabitacion(num, piso, tipo, precio, disp)  # Probar el índice con i en self.__listaHoteles
        archivo.close()

    # Inciso 1)
    def agregarHabitacionManual(self, nomHotel):
        encontrado = False
        i = 0
        while not encontrado and i < len(self.__listaHoteles):
            if self.__listaHoteles[i].getNombre().lower() == nomHotel.lower():
                encontrado = True
                num = int(input("Ingrese el número de habitación: "))
                piso = int(input("Ingrese el piso: "))
                tipo = input("Ingrese el tipo de habitación: ")
                precio = float(input("Ingrese el precio por noche: $"))
                self.__listaHoteles[i].agregarHabitacion(num, piso, tipo, precio, disp=True)

            else:
                i += 1
        
        if not encontrado:
            print("\nERROR - El hotel ingresado no existe.")

    # Inciso 2)
    def reservarHabitacion(self, nomHotel):
        opcion = 1
        encontrado = False
        i = 0
        while not encontrado and i < len(self.__listaHoteles):
            if self.__listaHoteles[i].getNombre().lower() == nomHotel.lower():
                encontrado = True
                numHabitacion = int(input("Ingrese el número de habitación: "))
                self.__listaHoteles[i].buscarHabitacion(numHabitacion, opcion)
            
            else:
                i += 1

        if not encontrado:
            print("\nERROR - El hotel ingresado no existe.")

    # Inciso 3)
    def liberarHabitacion(self, nomHotel):
        opcion = 2
        encontrado = False
        i = 0
        while not encontrado and i < len(self.__listaHoteles):
            if self.__listaHoteles[i].getNombre().lower() == nomHotel.lower():
                encontrado = True
                numHabitacion = int(input("Ingrese el número de la habitación que desea liberar: "))
                self.__listaHoteles[i].buscarHabitacion(numHabitacion, opcion)

            else:
                i += 1

        if not encontrado:
            print("\nERROR - El hotel ingresado no existe.")
    
    # Inciso 4)
    def infoTipoHabitacion(self, tipo):
        encontrado = False
        for hotel in self.__listaHoteles:
            nomHotel = hotel.getNombre()
            if hotel.mostrarNumeroYPiso(tipo, nomHotel):
                encontrado = True

        if not encontrado:
            print("ERROR - No existen habitaciones con el tipo ingresado.")

    # Inciso 5)
    def mostrarHabitacionesLibres(self):
        for hotel in self.__listaHoteles:
            hotel.mostrarCantLibresPorPiso(hotel.getNombre())

    # Inciso 6)
    def mostrarListado(self):
        for hotel in self.__listaHoteles:
            hotel.listarHabitaciones(hotel.getNombre())