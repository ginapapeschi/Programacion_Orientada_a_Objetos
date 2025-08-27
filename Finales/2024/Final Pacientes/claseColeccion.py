import csv
from claseNodo import Nodo
from clasePacientes import Paciente
from claseConObra import PacienteConObra
from claseHospitalizados import PacienteHospitalizado

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
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            dato = self.__actual.getDato()
            self.__actual = self.__actual.getSiguiente()
            self.__indice += 1
            return dato
    
    def insertarAlFinal(self, paciente):
        actual = self.__comienzo
        nuevoNodo = Nodo(paciente)

        if self.__comienzo is None:
            self.__comienzo = nuevoNodo
            self.__actual = nuevoNodo

        else:
            while actual.getSiguiente() is not None:
                actual = actual.getSiguiente()

            actual.setSiguiente(nuevoNodo)

        self.__tope += 1
        print("Paciente agregado")

    def cargarCSVPacientes(self):
        archivo = open('pacientes.csv', encoding='utf-8')
        reader = csv.reader(archivo, delimiter=',')
        for fila in reader:
            if fila[0] == 'P':
                paciente = Paciente(fila[1], fila[2], fila[3], fila[4])
            elif fila[0] == 'O':
                if fila[6] == '':
                    alergias = '-'
                else:
                    alergias = fila[6]
                paciente = PacienteConObra(fila[1], fila[2], fila[3], fila[4], fila[5], alergias, fila[7])
            elif fila[0] == 'H':
                paciente = PacienteHospitalizado(fila[1], fila[2], fila[3], fila[4], int(fila[5]), fila[6], fila[7], int(fila[8]), float(fila[9]))
            
            self.insertarAlFinal(paciente)
        archivo.close()

    # Inciso b
    def contarPacientesConNeumoniaYAmbulatorios(self):
        contNeumonia = 0
        contAmbulatorios = 0

        actual = self.__comienzo
        while actual != None:
            if isinstance(actual.getDato(), PacienteHospitalizado):
                if actual.getDato().getDiagnostico().lower() == 'neumonía':
                    contNeumonia += 1
            
            elif isinstance(actual.getDato(), PacienteConObra):
                contAmbulatorios += 1
            
            actual = actual.getSiguiente()

        print(f"\nPacientes hospitalizados con neumonía: {contNeumonia}")
        print(f"Pacientes ambulatorios: {contAmbulatorios}")
            
    # Inciso c
    def mostrarImporteCobrado(self):
        importeTotal = 0
        actual = self.__comienzo
        while actual != None:
            importeTotal += actual.getDato().calcularImporteCobrado()
            actual = actual.getSiguiente()
        
        print(f"\nImporte total cobrado por la clínica: ${importeTotal:.2f}")

    # Inciso d
    def indicarPacientePorPosicion(self, pos):
        if pos < 1 or pos > self.__tope:
            raise IndexError("\nERROR - Índice fuera de rango")
        else:
            actual = self.__comienzo

            for i in range(pos - 1):
                actual = actual.getSiguiente()
            
            if isinstance(actual.getDato(), PacienteConObra):
                tipoPaciente = 'ambulatorio'
            elif isinstance(actual.getDato(), PacienteHospitalizado):
                tipoPaciente = 'hospitalizado'
            else:
                tipoPaciente = 'normal'

            print(f"El paciente que se encuentra en la posición {pos} de la colección es {tipoPaciente}")

    # Inciso e
    def cambiarValorConsulta(self, nuevoValor):
        Paciente.setValorConsulta(nuevoValor)