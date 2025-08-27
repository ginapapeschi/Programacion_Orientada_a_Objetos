import csv
from claseMatriculas import Matricula

class GestorMatricula:
    __listaMatris: list

    def __init__(self):
        self.__listaMatris = []

    def agregarMatricula(self, unaMatri):
        self.__listaMatris.append(unaMatri)
        print("Matrícula cargada")

    def cargarCSVMatriculas(self, gestorEmpleados, gestorProgramas):
        archivo = open('matriculas.csv', encoding='utf-8')
        reader = csv.reader(archivo, delimiter=';')
        next(reader)
        for fila in reader:
            empleado = gestorEmpleados.buscarEmpleado(fila[1])
            programa = gestorProgramas.buscarPrograma(fila[2])
            if empleado != None and programa != None:
                matricula = Matricula(fila[0], empleado, programa)
                self.agregarMatricula(matricula)
        archivo.close()

    def mostrarMatriculas(self):
        for matricula in self.__listaMatris:
            print(matricula)

    # Inciso 1
    def informarDuracion(self, idEmpleado, gestorEmp):
        encabezado = False
        encontrado = False
        acum = 0
        empleado = gestorEmp.buscarEmpleadoPorID(idEmpleado)            # Como sólo se cuenta con un dato se realiza una búsqueda para saber si existe
        if empleado:
            for matricula in self.__listaMatris:
                if matricula.getEmpleado().getID() == empleado.getID():
                    encontrado = True
                    acum += matricula.getPrograma().getDuracion()       # Como ya tengo el objeto, se opera directamente con la matrícula
                    if not encabezado:
                        print(f"Duración de los programas de capacitación en los que está matriculado/a el/la empleado/a {empleado.getNombre()}:")
                        encabezado = True
                    print(f"- {matricula.getPrograma().getNombre()} - Duración: {matricula.getPrograma().getDuracion()} horas")
                                

            if encontrado:
                print(f"- Total: {acum} horas")

            else:
                print("\nERROR - El empleado no está matriculado en ningún programa.")

    # Inciso 2
    def informarEmpleadosMatriculados(self, nomPrograma, gestorProg):
        encontrado = False
        encabezado = False
        programa = gestorProg.buscarPrograma(nomPrograma)
        if programa:
            for matricula in self.__listaMatris:
                if matricula.getPrograma().getNombre() == programa.getNombre():
                    encontrado = True
                    if not encabezado:
                        print(f"Empleados matriculados:")
                        encabezado = True
                    print(f"- {matricula.getEmpleado().getNombre()}")
            
            if not encontrado:
                print("\nERROR - No hay empleados matriculados en el programa ingresado.")

        else:
            print("\nERROR - Programa no encontrado.")
                    
    # Inciso 3
    def buscarEmpleadoMatriculado(self, nomEmpleado):
        encontrado = False
        i = 0
        while not encontrado and i < len(self.__listaMatris):
            if self.__listaMatris[i].getEmpleado().getNombre() == nomEmpleado:
                encontrado = True

            else:
                i += 1
        
        return encontrado
            
            
