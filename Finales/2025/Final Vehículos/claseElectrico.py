import csv

from claseVehiculo import Vehiculo
from claseBateria import Bateria

class Electrico(Vehiculo):
    __autonomiaKM: float
    __baterias: list
    __eficiencia: float

    def __init__(self, pat, cap, km, autonomia, efi):
        super().__init__(pat, cap, km)
        self.__autonomiaKM = autonomia
        self.__eficiencia = efi
        self.__baterias = []

    def __str__(self):
        return f'''{super().__str__()}
Autonomía en KM: {self.__autonomiaKM}
Eficiencia: {self.__eficiencia}'''

    def agregarBateria(self, patente, capacidad, carga):
        unaBateria = Bateria(patente, capacidad, carga)
        if unaBateria in self.__baterias:
            print("Batería ya asignada")
        else:
            self.__baterias.append(unaBateria)
            print("Bateria agregada")

    def mostrarBaterias(self):
        print("BATERÍAS")
        for bateria in self.__baterias:
            print()
            print(bateria)

    def getAutonomia(self):
        return self.__autonomiaKM
    
    def getEficiencia(self):
        return self.__eficiencia
    
    def getPatente(self):
        return super().getPatente()
    
    def calcularConsumo(self, km=None):
        if km is None:
            km = super().getKmARecorrer()
        return km * self.__eficiencia
    
    def getCantidadPasajeros(self):
        return super().getCapacidad()
    
    # Inciso 1
    def cargarCSV(self):
        archivo = open('Baterias.csv', encoding='utf-8')
        reader = csv.reader(archivo, delimiter=';')
        next(reader)
        for fila in reader:
            if fila[0].lower() == super().getPatente().lower():
                patente = fila[0]
                capacidad = float(fila[1])
                carga = float(fila[2])
                self.agregarBateria(patente, capacidad, carga)
                if len(self.__baterias) < 4:
                    print()
                    print(f"Faltan baterías. Hay: {len(self.__baterias)}")
                else:
                    print()
                    print("Se alcanzó el mínimo de baterías")
                    print()
        
        archivo.close()

    # Inciso 2
    def getEnergiaDisponible(self):
        energia = 0
        for bateria in self.__baterias:
            energia += bateria.calcularEnergiaDisponible()

        return energia
