import csv
from claseDepartamento import Departamento
from claseAccidente import Accidente

class GestorDepto:
    __lista: list

    def __init__(self):
        self.__lista = []

    def agregarDepto(self, unDepto):
        self.__lista.append(unDepto)
    
    def cargarDeptos(self):
        archivo = open('Departamentos.csv', encoding='utf-8')
        reader = csv.reader(archivo, delimiter=';')
        band = True
        for fila in reader:
            if band:
                band = False
            else:
                depto = Departamento(int(fila[0]), fila[1])
                self.agregarDepto(depto)
                print("Departamento cargado")
        archivo.close()

    def incisoA(self, nroMes, tablaAccidentes):
        print(f"\nAccidentes registrados en el mes {nroMes}:")
        for depto in self.__lista:
            print(f"    Departamento: {depto.getNombreDepto()}")
            print(f"    Cantidad de accidentes: {tablaAccidentes.getAccidentesPorMes(depto.getID(), nroMes)}")

    def incisoB(self, nroMes, tablaAccidentes):
        deptoMax = tablaAccidentes.getMaxAccidentes(nroMes)
        if deptoMax != -1:
            print(f"\nEl departamento con mayor cantidad de accidentes es {self.__lista[deptoMax].getNombreDepto()}, con {tablaAccidentes.getCantAccidentesPorIndice(deptoMax + 1, nroMes)} accidentes registrados.")
        else:
            print("\nNo se registraron accidentes en el mes ingresado.")

    def incisoC(self, nomDepto, tablaAccidentes):
        encontrado = False
        i = 0
        while not encontrado and i < len(self.__lista):
            if nomDepto.lower() == self.__lista[i].getNombreDepto().lower():
                encontrado = True
                id = self.__lista[i].getID()
                total_accidentes = tablaAccidentes.getAccidentesPorDepto(id)
            else:
                i += 1

        if encontrado:
            if total_accidentes != 0:
                print(f"\nEl total de accidentes ocurridos en {nomDepto} es: {total_accidentes}")
            else:
                print(f"\nNo se registraron accidentes para el departamento ingresado.")

        else:
            print("\nNo se encontró el departamento ingresado.")

    def incisoD(self, tablaAccidentes):
        print(f"{'Departamento':<20}", end="")
        for i in range(12):
            print(f"{i + 1:>4}", end="")
        print()

        for depto in self.__lista:
            print(f"{depto.getNombreDepto():<20}", end="")
            id = depto.getID()
            for j in range(12):
                accidentes = tablaAccidentes.getAccidentesPorMes(id, j + 1)
                print(f"{accidentes:>4}", end="")
            print()

        # Mostrar línea de totales
        print(f"{'TOTAL':<20}", end="")
        for j in range(12):
            totalMes = 0
            for depto in self.__lista:
                id = depto.getID()
                totalMes += tablaAccidentes.getAccidentesPorMes(id, j + 1)
            print(f"{totalMes:>4}", end="")
        print()