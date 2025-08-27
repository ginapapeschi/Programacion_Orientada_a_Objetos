from clasePacientes import Paciente

class PacienteHospitalizado(Paciente):
    __numHabitacion: int
    __fechaIngreso: str
    __diagnostico: str
    __cantDiasInternacion: int
    __importeDescartables: float

    def __init__(self, nom, ap, email, num, numHab, fecha, diag, cantDias, importe):
        super().__init__(nom, ap, email, num)
        self.__numHabitacion = numHab
        self.__fechaIngreso = fecha
        self.__diagnostico = diag
        self.__cantDiasInternacion = cantDias
        self.__importeDescartables = importe

    def __str__(self):
        return f'''{super().__str__()}
Número de habitación: {self.__numHabitacion}
Fecha de ingreso: {self.__fechaIngreso}
Diagnóstico: {self.__diagnostico}
Cantidad de días de internación: {self.__cantDiasInternacion}
Importe en concepto de descartables: ${self.__importeDescartables:.2f}'''

    def getNumHabitacion(self):
        return self.__numHabitacion
    
    def getFechaIngreso(self):
        return self.__fechaIngreso
    
    def getDiagnostico(self):
        return self.__diagnostico
    
    def getCantDiasInternacion(self):
        return self.__cantDiasInternacion
    
    def getImporte(self):
        return self.__importeDescartables
    
    def calcularImporteCobrado(self):
        return self.__cantDiasInternacion * 150000 + self.__importeDescartables
    