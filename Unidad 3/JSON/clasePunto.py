import json
from pathlib import Path

class Punto:
    __x: int
    __y: int

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f"(x,y) = ({self.__x}, {self.__y})"
    
    def toJSON(self): # Serializa un objeto (lo convierte en diccionario).
        d = dict(__class__ = self.__class__.__name__,
                 # __class__ es un atributo de cualquier objeto que dice a qué clase PERTENECE el objeto.
                 # self.__class__ hace referencia a la clase del objeto (Punto en este caso).
                 # .__name__ obtiene el nombre de la clase como string ("Punto").
                 # Entonces self.__class__ devuelve la clase del objeto, y .__name__ devuelve el nombre como string.
                 # En definitiva, guarda el nombre de la clase en __class__ para guardarlo en el diccionario, es decir, registra el TIPO DE DATO del objeto dentro del diccionario que se guardará como JSON.

                 __atributos__ = dict(x = self.__x, y = self.__y))
        
        return d
        # Devuelve un diccionario con el nombre de la clase y sus atributos, listo para ser transformado en JSON.

class Manejador:
    __puntos: list

    def __init__(self):
        self.__puntos = []

    def agregarPunto(self, unPunto):
        self.__puntos.append(unPunto)
        print("Punto agregado")

    def mostrarDatos(self):
        for punto in self.__puntos:
            print(punto)

    def toJSON(self):
        d = dict(__class__ = self.__class__.__name__, 
                # Guarda el nombre de la clase del objeto como texto.
                 puntos = [punto.toJSON() for punto in self.__puntos])
        '''
                listaPuntos = []
                for punto in self.__puntos:
                    listaPuntos.append(punto.toJSON())
        ''' # Se recorren todos los puntos guardados en self.__puntos y a cada uno se le aplica toJSON()
        
        return d
        # Convierte el manejador y todos los puntos dentro en un diccionario, listo para ser transformado en JSON.

class ObjectEncoder:   # Gestiona la conversión entre objetos y texto/diccionario
    def decodificarDiccionario(self, d):
    # Convierte un diccionario que representa un objeto en un objeto Python real.

        if '__class__' not in d:        # Si no tiene clave __class__, no es un diccionario, así que lo devuelve
        # Verifica si el diccionario d tiene la clave "__class__", la que se colocó al convertir un objeto en diccionario para saber qué clase es.
            return d
        # Si no tiene "__class__", no es un objeto que fue convertido en diccionario, por lo que lo devuelve sin modificar. Esto es importante ya que pueden haber partes que no son objetos convertidos en diccionarios (serializados), sino números, strings, listas o diccionarios comunes. Por ejemplo, 
            '''
        { 
            "nombre": "Ana",
            "edad": 30
        }
            '''
        # No tiene "__class__", por lo que no es un objeto serializado y no hay que convertirlo a nada.
        
        else:
            className = d['__class__']
            # Obtiene el nombre de la clase desde el diccionario (Punto o Manejador). Se usa como subíndice la clave para obtener el valor.

            class_ = eval(className)     # Convierte ese nombre (string) en una clase REAL.
            # eval() evalúa una cadena de texto como si fuera código Python. Si eval(className) donde className = "Manejador", entonces eval("Manejador") convierte el texto "Manejador" en la clase real Manejador. Un ejemplo, pero con la clase Punto:
            '''
            obj = class_(x=3, y=4) que equivale a
            obj = Punto(x=3, y=4)
            '''

            if className == 'Manejador': # Si es un Manejador, RECONSTRUYE todos los puntos guardados.
                # Se fija si el objeto que se quiere reconstruir es un Manejador.
                listaPuntosSerializados = d['puntos']
                # Obtiene la lista de puntos serializados (como diccionarios), guardadas a través del toJSON() del Manejador. Es decir, se accede al valor asociado a la clave "puntos" dentro del diccionario d. Ese valor es una lista de puntos serializados, que fue guardada en el archivo JSON y reconstruida como lista de diccionarios. Esta clave viene de toJSON().
                # Es un diccionario con la información de los puntos, listo para deserializar (convertirlo en objeto).

                manejador = class_()
                # Se reconstruye un nuevo Manejador vacío, ya que class_ tiene asociada la clase Manejador.

                for diccionarioPunto in listaPuntosSerializados:    
                    # Por cada punto, lo reconstruye con los atributos (x, y) y lo agrega al manejador.
                    # Recorre cada uno de los elementos de la lista de puntos en forma de diccionario. Cada diccionarioPunto es algo como:
                    '''
                    {
                        "__class__": "Punto",
                        "__atributos__": {"x": 3, "y": 4}
                    }                    
                    '''
                    className = diccionarioPunto.pop('__class__')
                    # Extrae el valor de la clave "__class__" y lo guarda en className (guarda "Punto"). A la vez, elimina esa clave del diccionarioPunto (con el método pop()), quedando en el diccionario solamente la clave __atributos__. Equivalente a:
                    '''
                    className = diccionarioPunto['__class__'] # Accede al valor sin eliminarlo.
                    del diccionarioPunto['__class__']         # Elimina la clave del diccionario
                    '''
                    # __class__ se elimina porque luego se espera que el diccionario sólo tenga atributos para crear el objeto. Ya se conoce el tipo del objeto (la clase), sólo faltan los atributos.

                    class_ = eval(className)
                    # Se convierte el string "Punto" almacenado en className en la clase real Punto, y ahora class_ apunta a la clase Punto.

                    atributos = diccionarioPunto['__atributos__']
                    # Esta línea accede al valor asociado a la clave '__atributos__', que es otro diccionario. Pasa de:
                    '''
                    diccionarioPunto = {
                        "__atributos__": {"x": 3, "y": 4}
                    }

                    a

                    atributos = {"x": 3, "y": 4}
                    '''
                    # Es decir, se almacena en "atributos" el diccionario que se accedía a través de la clave "__atributos__".

                    unPunto = class_(**atributos)
                    # Se instancia un nuevo objeto. class_ es la clase Punto, y **atributos son los valores que se mandan por parámetros (desempaqueta el diccionario como argumentos con nombre). Sería el equivalente a escribir:
                    '''
                    unPunto = class_(**{"x": 3, "y": 4}), que es exactamente igual a:
                    unPunto = class_(x = atributos["x"], y = atributos["y"]), lo mismo que:
                    unPunto = Punto(x=3, y=4)
                    '''
                    # **atributos sirve para pasar un diccionario sin reescribir código y no es necesario saber exactamente cuántos o cuáles atributos tiene.

                    manejador.agregarPunto(unPunto)
                    # Agrega el punto recién reconstruido al Manejador.
            
            return manejador
        
    def guardarJSONArchivo(self, diccionario, archivo):
        with Path(archivo).open("w", encoding='UTF-8') as destino:
            json.dump(diccionario, destino, indent=4)
            destino.close()
            print("Puntos guardados")

    def leerJSONArchivo(self, archivo):
        with Path(archivo).open(encoding='UTF-8') as fuente:
            diccionario = json.load(fuente)
            fuente.close()
            
            return diccionario
        
    def convertirTextoADiccionario(self, texto):
        return json.loads(texto)
    

class Menu:
    def mostrarMenu(self):
        print()
        print("MENÚ DE OPCIONES".center(60))
        print('''
1 - Crear un Punto
2 - Guardar Puntos en Archivo
3 - Leer datos de Puntos
4 - Mostrar datos Puntos
5 - Salir''')
        opcionCorrecta = False
        while not opcionCorrecta:
            opcion = int(input("\nSeleccione un número del 1 al 5: "))
            if opcion in [1, 2, 3, 4, 5]:
                opcionCorrecta = True
        return opcion
    

if __name__ == '__main__':
    jsonF = ObjectEncoder()
    ManejadorPuntos = Manejador()
    bandera = True
    while bandera:
        menu = Menu()
        opcion = menu.mostrarMenu()
        if opcion == 1:
            print("\nCreando un nuevo Punto")
            x = int(input("Coordenada x: "))
            y = int(input("Coordenada y: "))
            punto = Punto(x, y)
            ManejadorPuntos.agregarPunto(punto)

        elif opcion == 2:
            d = ManejadorPuntos.toJSON()
            jsonF.guardarJSONArchivo(d, 'datosPuntos.json')
        
        elif opcion == 3:
            diccionario = jsonF.leerJSONArchivo('datosPuntos.json')
            # Se lee el archivo JSON y se obtiene un diccionario con los datos serializados (en diccionario).
            ManejadorPuntos = jsonF.decodificarDiccionario(diccionario)
            # Se almacena un Manejador completo decodificado y reconstruido a partir del diccionario leído.

        elif opcion == 4:
            ManejadorPuntos.mostrarDatos()

        else:
            bandera = False 
            print("\nPrograma finalizado")