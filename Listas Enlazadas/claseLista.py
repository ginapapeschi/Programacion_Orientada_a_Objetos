from claseNodo import Nodo

class Lista:
    __comienzo: Nodo
    __actual: Nodo
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
            self.__indice = 0   # Reinicia el índice que controla la iteración (el típico i del for).
            raise StopIteration
        
        else:
            self.__indice += 1
            persona = self.__actual.getDato()
            self.__actual = self.__actual.getSiguiente()
            return persona
        
    def insertarPorCabeza(self, persona):
        nuevoNodo = Nodo(persona)
        nuevoNodo.setSiguiente(self.__comienzo)
        self.__comienzo = nuevoNodo
        self.__actual = nuevoNodo
        self.__tope += 1
        print("Nodo insertado")

    def insertarPorPosicion(self, persona, pos):
        if pos < 0 or pos > self.__tope:
            raise IndexError("\nERROR - Posición no válida.")

        else:
            nuevoNodo = Nodo(persona)

        if pos == 0:
            # Insertar al principio.
            nuevoNodo.setSiguiente(self.__comienzo)
            self.__comienzo = nuevoNodo
            self.__actual = nuevoNodo
            
        else:
            # Insertar entre nodos.
            actual = self.__comienzo
            for i in range(pos-1):
                actual = actual.getSiguiente()  # Avanza hasta el nodo anterior a la posición deseada.

            nuevoNodo.setSiguiente(actual.getSiguiente()) # Al nuevo nodo le asigna como siguiente el nodo en la posición deseada (el que será desplazado), para no perder el enlace con el resto de la lista.
            actual.setSiguiente(nuevoNodo)      # El nodo anterior a la posición deseada le asigna como siguiente el nuevo nodo, insertándolo en la lista.

        self.__tope += 1
        print("Nodo insertado")


    '''
    Forma más intuitiva de entenderlo:

    anteriorAlDeseado = self.__comienzo
    for i in range(pos-1):
        anteriorAlDeseado = anteriorAlDeseado.getSiguiente()
    
    siguienteAlDeseado = anteriorAlDeseado.getSiguiente()
    nuevoNodo.setSiguiente(siguienteAlDeseado)
    anteriorAlDeseado.setSiguiente(nuevoNodo)

    '''

    def insertarAlFinal(self, persona):
        nuevoNodo = Nodo(persona)

        if self.__comienzo is None:
            # Lista vacía: el nuevo nodo es el comienzo.
            self.__comienzo = nuevoNodo
            self.__actual = nuevoNodo
        
        else:
            actual  = self.__comienzo
            while actual.getSiguiente() is not None: # Recorre hasta el último nodo.
                actual = actual.getSiguiente()

            actual.setSiguiente(nuevoNodo)           # El siguiente del último nodo será el nuevo nodo.

        self.__tope += 1
        print("Nodo insertado")
            
    def mostrarPersonas(self):
        aux = self.__comienzo

        while aux != None:
            print(aux.getDato())
            aux = aux.getSiguiente()

    def buscarPersonaPorDNI(self, dni):
        aux = self.__comienzo

        while aux is not None:
            if aux.getDato().getDNI() == dni:
                return aux.getDato()
            
            else:
                aux = aux.getSiguiente()

        print("\nNo se encontró la persona con el DNI ingresado.")

    def eliminarPorDNI(self, dni):
        actual = self.__comienzo
        anterior = None
        encontrado = False

        while actual is not None and not encontrado:
            if actual.getDato().getDNI() == dni:
                encontrado = True

            else:
                anterior = actual
                actual = actual.getSiguiente()

        if encontrado:
            print(f"Persona encontrada: {actual.getDato().getNombre()} {actual.getDato().getApellido()}")
            if anterior is None:
                # El elemento a eliminar es la cabeza.
                self.__comienzo = actual.getSiguiente()

            else:
                anterior.setSiguiente(actual.getSiguiente())
            
            self.__tope -= 1
            del actual

        else:
            print("\nNo se encontró la persona con el DNI ingresado.")