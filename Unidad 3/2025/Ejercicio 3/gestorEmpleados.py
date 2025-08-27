import csv
from claseEmpleados import Empleado

class GestorEmpleado:
    __listaEmpleados: list

    def __init__(self):
        self.__listaEmpleados = []

    def agregarEmpleado(self, unEmpleado):
        self.__listaEmpleados.append(unEmpleado)
        print("Empleado cargado")

    def cargarCSVEmpleados(self):
        archivo = open('empleados.csv', encoding='utf-8')
        reader = csv.reader(archivo, delimiter=';')
        next(reader)
        for fila in reader:
            empleado = Empleado(fila[0], int(fila[1]), fila[2])
            self.agregarEmpleado(empleado)
        archivo.close()

    def buscarEmpleado(self, nomEmpleado):
        i = 0
        while i < len(self.__listaEmpleados):
            if self.__listaEmpleados[i].getNombre().lower() == nomEmpleado.lower():
                return self.__listaEmpleados[i]
            
            else:
                i += 1

    # Inciso 1
    def buscarEmpleadoPorID(self, idEmpleado):
        i = 0
        while i < len(self.__listaEmpleados):
            if self.__listaEmpleados[i].getID() == idEmpleado:
                return self.__listaEmpleados[i]
            
            else:
                i += 1
        
        print("\nERROR - No se encontró el empleado con el ID ingresado.")

    # Inciso 3
    def informarNoMatriculados(self, gestorMatri):
        encontrado = False
        encabezado = False
        for empleado in self.__listaEmpleados:
            matriculado = gestorMatri.buscarEmpleadoMatriculado(empleado.getNombre())
            if not matriculado:
                encontrado = True
                if not encabezado:
                    print("\nEmpleados no matriculados en ningún programa:")
                    encabezado = True
                print(f"- {empleado.getNombre()}")

            
        if not encontrado:
            print("\nNo hay empleados sin matricular.")