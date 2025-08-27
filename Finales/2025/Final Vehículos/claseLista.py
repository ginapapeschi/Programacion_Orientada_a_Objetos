import csv

from claseNodo import Nodo
from claseColectivo import Colectivo
from claseElectrico import Electrico

class Lista:
    __comienzo: object
    __actual: object
    __indice: int
    __tope: int

    def __init__(self):
        self.__comienzo = None
        self.__actual = None
        self.__indice = 0
        self.__tope = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__indice == self.__tope:
            self.__indice = 0
            self.__actual = self.__comienzo
            raise StopIteration
        else:
            dato = self.__actual.getDato()
            self.__actual = self.__actual.getSiguiente()
            self.__indice += 1
            return dato

    def agregarVehiculo(self, vehiculo):
        nuevoNodo = Nodo(vehiculo)
        nuevoNodo.setSiguiente(self.__comienzo)
        self.__comienzo = nuevoNodo
        self.__actual = nuevoNodo
        self.__tope += 1
        print("Vehículo agregado")

    # Inciso 1
    def cargarCSV(self):
        archivo = open('Vehiculos.csv', encoding='utf-8')
        reader = csv.reader(archivo, delimiter=';')
        next(reader)
        for fila in reader:
            if fila[0] == 'C':
                unColectivo = Colectivo(fila[1], int(fila[2]), float(fila[3]), fila[4], float(fila[5]), fila[6])
                self.agregarVehiculo(unColectivo)

            elif fila[0] == 'E':
                unElectrico = Electrico(fila[1], int(fila[2]), float(fila[3]), float(fila[4]), float(fila[5]))
                self.agregarVehiculo(unElectrico)
                if unElectrico:
                    unElectrico.cargarCSV()

        archivo.close()

    # Inciso 2
    def listarPatentes(self, distancia):
        encabezado = False
        hay = False
        actual = self.__comienzo
        
        while actual != None:
            if isinstance(actual.getDato(), Electrico):
                vehiculo = actual.getDato()
                totalDisponible = vehiculo.getEnergiaDisponible() - vehiculo.calcularConsumo(distancia)
                if totalDisponible > 0:
                    if not encabezado:
                        print()
                        print(f"Patente de vehículos eléctricos que pueden recorrer {distancia}km: ")
                        encabezado = True
                    print(f"- {vehiculo.getPatente()}")
                    hay = True
                
            actual = actual.getSiguiente()

        if not hay:
            print(f"ERROR - No hay vehículos que puedan recorrer hasta {distancia}km con la energía disponible. Energía disponible: {vehiculo.getEnergiaDisponible():.2f}kwh - Consumo en {distancia}km: {vehiculo.calcularConsumo(distancia)}kwh")

    # Inciso 3
    def mostrarVehiculos(self):
        print()
        print("VEHÍCULOS: ")
        actual = self.__comienzo

        while actual != None:
            print()
            print(f"Patente: {actual.getDato().getPatente()} - Cantidad de pasajeros: {actual.getDato().getCantidadPasajeros()} - Tipo de vehículo: {actual.getDato().__class__.__name__} - Consumo por kilómetro: {actual.getDato().calcularConsumo():.2f}")
            actual = actual.getSiguiente()

    # Inciso 4
    def agregarManual(self, pos):
        if pos < 0 or pos > self.__tope:
            raise IndexError("ERROR - Posición no válida")

        else:
            patente = input("Ingrese la patente: ")
            capacidad = int(input("Ingrese la capacidad de pasajeros: "))
            kmARecorrer = float(input("Ingrese km a recorrer: "))
            nomEmpresa = input("Ingrese el nombre de la empresa: ")
            capComb = float(input("Ingrese la capacidad de combustible: "))
            tipoComb = input("Ingrese el tipo de combustible: ")
            unVehiculo = Colectivo(patente, capacidad, kmARecorrer, nomEmpresa, capComb, tipoComb)

            if unVehiculo:
                if pos == 0:
                    self.agregarVehiculo(unVehiculo)

                else:
                    nuevoNodo = Nodo(unVehiculo)
                    actual = self.__comienzo

                    for i in range(pos - 1):
                        actual = actual.getSiguiente()

                    nuevoNodo.setSiguiente(actual.getSiguiente())
                    actual.setSiguiente(nuevoNodo)
                    self.__tope += 1
                    print(f"Vehículo agregado en la posición {pos}")


