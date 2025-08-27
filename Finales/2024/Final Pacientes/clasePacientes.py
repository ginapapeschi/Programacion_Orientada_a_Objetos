class Paciente:
    __nombre: str
    __apellido: str
    __email: str
    __numTelefono: str
    __valorConsulta = 15000 # Variable de clase

    def __init__(self, nom, ap, email, num):
        self.__nombre = nom
        self.__apellido = ap
        self.__email = email
        self.__numTelefono = num
        
    def __str__(self):
        return f'''Nombre: {self.__nombre}
Apellido: {self.__apellido}
Email: {self.__email}
Número de teléfono: {self.__numTelefono}
Valor de consulta: ${self.__valorConsulta:.2f}'''
    
    def getNombre(self):
        return self.__nombre
    
    def getApellido(self):
        return self.__apellido
    
    def getEmail(self):
        return self.__email
    
    def getNumTelefono(self):
        return self.__numTelefono
    
    @classmethod
    def getValorConsulta(cls):
        return cls.__valorConsulta
    
    @classmethod
    def setValorConsulta(cls, valor):
        if valor < 0:
            print("\nERROR - Valor de consulta no válido")
        else:
            anterior = cls.__valorConsulta
            cls.__valorConsulta = valor
            print(f"Valor anterior: ${anterior:.2f} - Valor actual: ${valor:.2f}")

    def calcularImporteCobrado(self):
        return self.getValorConsulta()