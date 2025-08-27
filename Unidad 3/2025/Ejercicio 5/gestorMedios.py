import csv
from claseMedio import Medio
from claseTelevision import Television
from clasePrograma import Programa
from clasePrensa import Prensa
from claseRadio import Radio

class Nodo:
    __dato: None
    __sig: None

    def __init__(self, medio):
        self.__dato = medio
        self.__sig = None

    def getDato(self):
        return self.__dato
    
    def setSiguiente(self, siguiente):
        self.__sig = siguiente
    
    def getSiguiente(self):
        return self.__sig
    
# La clase Nodo debería ir en otro módulo para mayor orden.

class Lista:
    __comienzo: None
    __actual: None # Es un puntero a un OBJETO. Indica la posición actual en la lista.
    __indice: int  # Indica la posición actual en la lista, pero es un NÚMERO.
    # Ambos comparten la misma posición lógica, pero con propósitos diferentes.
    __tope: int

    def __init__(self):
        self.__comienzo = None
        self.__actual = None
        self.__indice = 0
        self.__tope = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__indice == self.__tope:    # Verifica si se recorrieron todos los elementos.
            # self.__indice es el contador de cuántos elementos se han ITERADO. self.__tope es la cantidad total de elementos.
            self.__actual = self.__comienzo # Como se recorrió todo, se resetea el actual al inicio de la lista.
            self.__indice = 0               # Se resetea el índice por el mismo motivo.
            raise StopIteration             # OBLIGATORIO para que los for sepan que la iteración terminó.
            # Los loops de while no necesitan de StopIteration, porque se maneja la iteración a diferencia de un for.

        else:
            self.__indice += 1              # Incrementa porque se devolverá un nuevo elemento del recorrido.
            dato = self.__actual.getDato()  # Se guarda el dato actual antes de avanzar el puntero.
            self.__actual = self.__actual.getSiguiente() # Avanza al siguiente nodo.
            return dato                     # Devuelve el dato del nodo actual antes de avanzar.
        
    def agregarMedio(self, unMedio):        # Se agrega un nuevo nodo en la CABEZA de la lista.
        nodo = Nodo(unMedio)
        nodo.setSiguiente(self.__comienzo)  # El nuevo nodo apunta al nodo que antes era la CABEZA de la lista.
        self.__comienzo = nodo
        self.__actual = nodo
        self.__tope += 1
        print("Medio cargado.")

    def cargarCSVMediosYProgramas(self):
        archivoMedios = open('medios.csv', encoding='utf-8')
        readerMedios = csv.reader(archivoMedios, delimiter=';')
        next(readerMedios)
        # Se abre el segundo CSV.
        archivoProgramas = open('programa.csv', encoding='utf-8')
        readerProgramas = csv.reader(archivoProgramas, delimiter=';')
        next(readerProgramas)
        listaProgramas = list(readerProgramas) # Se lo guarda en una lista para luego poder recorrerla múltiples veces.

        for fila1 in readerMedios:
            if fila1[0] == 'T':
                nombre = fila1[1]
                audiencia = int(fila1[2])
                canal = int(fila1[3])
                cantProgramas = int(fila1[4])
                tele = Television(nombre, audiencia, canal, cantProgramas)
                # Segundo for para buscar los programas cuyo segundo campo (canal) coincida con el canal del medio.
                for fila2 in listaProgramas:
                    if fila2[1] == str(canal):
                        nombre = fila2[2]
                        horaInicio = fila2[3]
                        horaFin = fila2[4]
                        programa = Programa(nombre, horaInicio, horaFin)
                        tele.agregarPrograma(programa) # Se agregan los programas a la instancia creada.
                self.agregarMedio(tele)

            elif fila1[0] == 'R':
                nombre = fila1[1]
                audiencia = int(fila1[2])
                emisora = fila1[5]
                frecuencia = fila1[6]
                radio = Radio(nombre, audiencia, emisora, frecuencia)
                # Se recorre la lista de programas comparando las frecuencias (frecuencia y fila2[1] "Canal"), ignorando mayúsculas, minúsculas y espacios.
                for fila2 in listaProgramas:
                    if fila2[1].strip().lower() == frecuencia.strip().lower():
                        nombre = fila2[2]
                        horaInicio = fila2[3]
                        horaFin = fila2[4]
                        programa = Programa(nombre, horaInicio, horaFin)
                        radio.agregarPrograma(programa)
                self.agregarMedio(radio)

            elif fila1[0] == 'P':
                nombre = fila1[1]
                audiencia = int(fila1[2])
                tipo = fila1[7]
                periodicidad = fila1[8]
                prensa = Prensa(nombre, audiencia, tipo, periodicidad)
                self.agregarMedio(prensa)
                # Se crea directamente el objeto Prensa, ya que no tiene programas asociados.

        archivoMedios.close()
        archivoProgramas.close()

    # Inciso 1
    def crearMedioManual(self):
        medio = None
        tipo = input("Ingrese el tipo de medio que desea insertar(T = Televisión/ R = Radio / P = Prensa): ").upper()

        if tipo == 'T':
            nombre = input("Ingrese el nombre del canal de TV: ")
            audiencia = int(input("Ingrese la audiencia: "))
            canal = int(input("Ingrese el número de canal: "))
            cantProgramas = int(input("Ingrese cantidad de programas: "))
            medio = Television(nombre, audiencia, canal, cantProgramas)
        
        elif tipo == 'R':
            nombre = input("Ingrese el nombre de la radio: ")
            audiencia = int(input("Ingrese la audiencia: "))
            nomEmisora = input("Ingrese el nombre de la emisora: ")
            frecuencia = input("Ingrese la frecuencia (en MHz): ")
            medio = Radio(nombre, audiencia, nomEmisora, frecuencia)

        elif tipo == 'P':
            nombre = input("Ingrese el nombre de la prensa: ")
            audiencia = int(input("Ingrese la audiencia: "))
            tipoPubli = input("Ingrese el tipo de publicación (diario o revista): ")
            periodicidad = input("Ingrese la periodicidad: ")
            medio = Prensa(nombre, audiencia, tipoPubli, periodicidad)

        else:
            print("\nERROR - Tipo de medio no válido.")

        return medio

    def agregarMedioPorPosicion(self, pos):
        if pos < 0 or pos > self.__tope:
            raise IndexError("\nERROR - Posición inválida.")
        
        else:
            medio = self.crearMedioManual()
            if medio:
                if pos == 0: # Agregar por cabeza
                    self.agregarMedio(medio)

                else:
                    actual = self.__comienzo
                    for i in range(pos-1):
                        actual = actual.getSiguiente()

                    nuevoNodo = Nodo(medio)
                    nuevoNodo.setSiguiente(actual.getSiguiente())
                    actual.setSiguiente(nuevoNodo)

                    self.__tope += 1
                    print("Medio insertado por posición.")

    # Inciso 2
    def agregarManual(self):
        medio = self.crearMedioManual()
        if medio:
            if isinstance(medio, Medio):
                self.agregarMedio(medio)
            else:
                raise TypeError("\nERROR - El objeto no pertenece a la clase Medio.")
        
    # Inciso 3
    def mostrarMedios(self):
        if self.__tope == 0:
            print("La lista se encuentra vacía.")
        else:
            print()
            print("------- MEDIOS -------".center(70))
            actual = self.__comienzo
            while actual is not None:
                print(actual.getDato().__class__.__name__, end=' - ') # Para obtener el nombre de la clase en string.
                print(actual.getDato())
                actual = actual.getSiguiente()
    
    def inciso4(self, nom):
        actual = self.__comienzo
        television = None

        while television is None and actual is not None:
            if isinstance(actual.getDato(), Television):
                television = actual.getDato().buscarProgramaPorNombre(nom)

            if television:
                print(f"Nombre del canal: {actual.getDato().getNombre()}")
                actual.getDato().getHorariosPrograma(nom)

            else:
                actual = actual.getSiguiente()

        if television is None:
            print("\nERROR - No se encontró el programa ingresado.")

    def inciso5(self, nom):
        actual = self.__comienzo
        encontrado = False
        
        while not encontrado and actual is not None:
            if isinstance(actual.getDato(), Radio):
                if actual.getDato().getEmisora().lower() == nom.lower():
                    encontrado = True
                    print()
                    print("------- PROGRAMACIÓN -------".center(70))
                    actual.getDato().mostrarProgramas()
                
            actual = actual.getSiguiente()
        
        if not encontrado:
            print("\nERROR - No se encontró la emisora.")

    def inciso6(self):
        actual = self.__comienzo
        cantDiarios = 0
        cantRevistas = 0

        while actual is not None:
            if isinstance(actual.getDato(), Prensa):
                if actual.getDato().getTipo() == 'Diario':
                    cantDiarios += 1
                
                elif actual.getDato().getTipo() == 'Revista':
                    cantRevistas += 1

            actual = actual.getSiguiente()

        if cantDiarios != 0 and cantRevistas != 0:
            print(f"Cantidad de diarios: {cantDiarios} - Cantidad de revistas: {cantRevistas}")
        else:
            print("\nNo se encontraron diarios ni revistas.")