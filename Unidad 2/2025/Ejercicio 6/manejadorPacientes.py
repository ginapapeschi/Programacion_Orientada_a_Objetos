import csv
from clasePaciente import Paciente

class ManejadorPaciente:
    __listaPac: list

    def __init__(self):
        self.__listaPac = []

    def agregarPaciente(self, unPaciente):
        self.__listaPac.append(unPaciente)

    def cargarCSVPacientes(self):
        archivo = open('pacientes.csv', encoding='utf-8')
        reader = csv.reader(archivo, delimiter=';')
        band = True
        for fila in reader:
            if band:
                band = False
            else:
                paciente = Paciente(fila[0], fila[1], fila[2])
                self.agregarPaciente(paciente)
                print("Paciente cargado.")
        archivo.close()

    def incisoB(self, dni, mAtenciones):
        encontrado = False
        i = 0
        while not encontrado and i < len(self.__listaPac):
            if self.__listaPac[i].getDNI() == dni:
                encontrado = True            
            else:
                i += 1
        
        if encontrado:
            cantAtenciones = mAtenciones.contarAtenciones(dni)
            if cantAtenciones > 0:
                if cantAtenciones == 1:
                    print(f"\nEl/la paciente {self.__listaPac[i].getNombre()} tuvo una sola atención.")
                else:
                    print(f"\nEl/la paciente {self.__listaPac[i].getNombre()} tuvo {cantAtenciones} atenciones.")
            else:
                print(f"\nEl/la paciente {self.__listaPac[i].getNombre()} no tuvo ninguna atención.")
        else:
            print("\nNo se encontró el DNI ingresado.")

    def incisoC(self, mAtenciones):
        hayPacientes = False
        print("\nListado de pacientes que no tuvieron ninguna atención:")
        for paciente in self.__listaPac:
            cantAtenciones = mAtenciones.contarAtenciones(paciente.getDNI())
            if cantAtenciones == 0:
                print(paciente)
                hayPacientes = True
        
        if not hayPacientes:
            print("\nListado vacío. No hay pacientes sin atención.")

    def incisoD(self):
        self.__listaPac.sort()
        print("\nLista de pacientes ordenados por unidad y apellido:")
        unidadActual = ""
        for paciente in self.__listaPac:
            if paciente.getUnidad() != unidadActual:
                unidadActual = paciente.getUnidad()
                print(f"\n----------{unidadActual}----------")
            print(f"- {paciente.getNombre()}")
            
            