from claseVehiculos import Vehiculo
from claseAutomoviles import Automovil
from claseCamiones import Camion

class GestorVehiculo:
    __listaVehiculos: list

    def __init__(self):
        self.__listaVehiculos = []

    # Inciso a
    def agregarVehiculo(self, tipoVehiculo, gestorRuta):
        nuevoVehiculo = None

        if tipoVehiculo.lower() in ['automóvil', 'automovil', 'camión', 'camion']:
            matricula = input("Ingrese matrícula: ")
            modelo = input("Ingrese modelo: ")
            costo = float(input("Ingrese el costo por kilómetro: $"))
            cantDias = int(input("Ingrese la cantidad de días de alquiler: "))

            if tipoVehiculo.lower() in ['automóvil', 'automovil']:
                maxPasajeros = int(input("Ingrese el máximo de pasajeros: "))
                cantPasajeros = int(input("Ingrese la cantidad de pasajeros a transportar: "))
                nuevoVehiculo = Automovil(matricula, modelo, costo, cantDias, maxPasajeros, cantPasajeros)

            else:
                capMax = float(input("Ingrese capacidad máxima de carga: "))
                cantCarga = float(input("Ingrese la cantidad transportada: "))
                if capMax < cantCarga:
                    print("\nERROR - La cantidad de carga excede a la capacidad máxima")
                else:
                    nuevoVehiculo = Camion(matricula, modelo, costo, cantDias, capMax, cantCarga)
                    gestorRuta.elegirRutas(nuevoVehiculo)

            if nuevoVehiculo:
                self.__listaVehiculos.append(nuevoVehiculo)
                print(f"Vehículo agregado - Tipo: {nuevoVehiculo.__class__.__name__.lower()}")

        else:
            print("\nERROR - Tipo de vehículo no válido")

    # Inciso b
    def buscarVehiculoPorMatricula(self, matricula):
        resultado = False
        i = 0
        while not resultado and i < len(self.__listaVehiculos):
            if self.__listaVehiculos[i].getMatricula().lower() == matricula.lower():
                resultado = self.__listaVehiculos[i]

            else:
                i += 1

        return resultado

    def mostrarInfoVehiculo(self, vehiculo):
        print()
        print(f"---- VEHÍCULO {vehiculo.getMatricula().upper()} ----".center(50))
        print(vehiculo)
        if isinstance(vehiculo, Camion):
            vehiculo.mostrarRutas()

    def incisoB(self, matricula):
        vehiculo = self.buscarVehiculoPorMatricula(matricula)
        if vehiculo:
            self.mostrarInfoVehiculo(vehiculo)

        else:
            raise Exception("\nERROR - Vehículo no encontrado")
        
    # Inciso c
    def mostrarVehiculos(self):
        print()
        print(f"---- VEHÍCULOS ----".center(50))
        for vehiculo in self.__listaVehiculos:
            print(f'''
            {vehiculo.__class__.__name__.upper()}
- Matrícula: {vehiculo.getMatricula()}
- Modelo: {vehiculo.getModelo()}
- Costo total del alquiler: ${vehiculo.calcularAlquiler():.2f}''')