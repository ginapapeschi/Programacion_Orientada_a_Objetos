from clasePacientes import Paciente

class PacienteConObra(Paciente):
    __historialMedico: str
    __alergias: str
    __obraSocial: str

    def __init__(self, nom, ap, email, num, historial, alergias, obra):
        super().__init__(nom, ap, email, num)
        self.__historialMedico = historial
        self.__alergias = alergias
        self.__obraSocial = obra

    def __str__(self):
        return f'''{super().__str__()}
Historial médico: {self.__historialMedico}
Alergias: {self.__alergias}
Obra social: {self.__obraSocial}'''

    def getHistorial(self):
        return self.__historialMedico
    
    def getAlergias(self):
        return self.__alergias
    
    def getObraSocial(self):
        return self.__obraSocial
    
    def calcularImporteCobrado(self):
        plus = 0
        consulta = super().getValorConsulta()

        if self.__obraSocial.lower() == 'obra social provincia':
            plus += 5000
        elif self.__obraSocial.lower() == 'obra social osde':
            plus += 2000
        else:
            plus += 10000

        importeACobrar = consulta + plus - consulta

        return importeACobrar