class Accidente:
    __tabla: list
    __cantFilas: int
    __cantColumnas: int

    def __init__(self):
        self.__tabla = []
        self.__cantFilas = 19
        self.__cantColumnas = 12

    def cerear(self):
        for i in range(self.__cantFilas):          # Recorre cada fila que se quiere crear
            fila = []                   # Inicializa una lista vacía para la nueva fila
            for j in range(self.__cantColumnas):   # Llena la variable 'fila' agregando 12 elementos (columnas)
                fila.append(0)          # Agrega un cero por cada columna para inicializar la fila
            self.__tabla.append(fila)   # Agrega la fila completa a la tabla principal (__tabla)
        
    def cargarTabla(self, depto, mes, cantAccidentes):
        self.__tabla[depto-1][mes-1] += cantAccidentes
        print(f"{cantAccidentes} accidentes registrados para el departamento {depto}, mes {mes}.")
    
    def getCantAccidentesPorIndice(self, nroDepto, nroMes):
        return self.__tabla[nroDepto-1][nroMes-1]

    # Inciso A y D
    def getAccidentesPorMes(self, nroDepto, nroMes):
        sum = 0
        sum += self.__tabla[nroDepto-1][nroMes-1]
        return sum
    
    # Inciso B
    def getMaxAccidentes(self, nroMes):
        max_accidentes = -1                 # Se empieza en -1 por si hay 0 accidentes en todos lados
        depto_max = -1
        for i in range(self.__cantFilas):   # Sólo se recorren filas (departamentos)
            if self.__tabla[i][nroMes-1] > max_accidentes:
                max_accidentes = self.__tabla[i][nroMes-1]
                depto_max = i
        return depto_max
    
    # Inciso C
    def getAccidentesPorDepto(self, nroDepto):
        totalAccidentes = 0
        for j in range(self.__cantColumnas):
            totalAccidentes += self.__tabla[nroDepto - 1][j]
        return totalAccidentes
    
    # Inciso D
    def getTotalAccidentesPorDepto(self, numDepto):
        sum = 0
        for j in range(self.__cantColumnas):
            sum += self.__tabla[numDepto - 1][j]
        return sum
