from ClaseMaterial import Material

class Ladrillo:
    __alto: int
    __largo: int
    __ancho: int
    __cant: int
    __id: int
    __kgMatPrimaUti: float
    __costo: float
    __materiales: list                                      # Agregación

    def __init__ (self, lar, anch, xcant, xid, kg, cost):
        self.__alto = 7
        self.__largo = 25
        self.__ancho = 15
        self.__cant = xcant
        self.__id = xid
        self.__kgMatPrimaUti = kg
        self.__costo = cost
        self.__materiales = []

    def agregarMaterial(self, nuevo):
        if nuevo not in self.__materiales:      # Verifica si el material ya está en la lista de materiales, por eso utiliza el "in", funcionando como un "for".
            self.__materiales.append(nuevo)
            print(f"Al ladrillo {self.__id} se le agrega el material {nuevo.getMaterial()}")                       # Notifica que el material fue agregado
        else:
            print(f"No se ha agregado material {nuevo.getMaterial()} al ladrillo {self.__id} porque ya lo tiene.") # Notifica que el material no fue agregado

    """
    def agregarMaterial(self, material):
    for mat in self.__materiales:                           # Verifica si el material ya está en la lista de materiales usando un bucle for.
        if mat == material:
            print(f"No se agrega el material {material.getMaterial()} al ladrillo {self.__identificador} porque ya lo tiene")
            return
    self.__materiales.append(material)                                                              # Si no se encontró el material, agregarlo a la lista
    print(f"Al ladrillo {self.__identificador} se le agrega el material {material.getMaterial()}")  # Notificar que el material ha sido agregado
    """

    def getMateriales(self):
        ret = ""
        if len(self.__materiales) > 0:                       # Verifica si la lista no está vacía.
            for unmaterial in self.__materiales:
                ret += str(unmaterial.getMaterial()) + ", "  # Convierte en string el material, lo concatena con otro separado de una coma y un espacio.
        return ret                                           # Si la lista está vacía retorna un espacio vacío "".

    @classmethod
    def getAlto(self):
        return self.__alto
    
    @classmethod
    def getLargo(self):
        return self.__largo
    
    @classmethod
    def getAncho(self):
        return self.__ancho
    
    def getCant(self):
        return self.__cant
    
    def getID(self):
        return self.__id
    
    def getKG(self):
        return self.__kgMatPrimaUti
    
    def getCosto(self):
        return self.__costo
    