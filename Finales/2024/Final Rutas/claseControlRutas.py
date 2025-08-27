import csv

from claseRutas import Ruta

class GestorRuta:
    __listaRutas: list

    def __init__(self):
        self.__listaRutas = []

    def agregarRuta(self, unaRuta):
        self.__listaRutas.append(unaRuta)
        print("Ruta agregada")

    def mostrarRutas(self):
        print()
        print("---- RUTAS ----".center(35))
        for ruta in self.__listaRutas:
            print()
            print(ruta)

    def cargaCSVRutas(self):
        archivo = open('Rutas.csv', encoding='utf-8')
        reader = csv.reader(archivo, delimiter=';')
        next(reader)
        for fila in reader:
            if fila[3].lower() == 'verdadero':
                asignado = True
            elif fila[3].lower() == 'falso':
                asignado = False
            unaRuta = Ruta(int(fila[0]), fila[1], float(fila[2].replace(',', '.')), asignado)
            self.agregarRuta(unaRuta)

        archivo.close()

    # Inciso a
    def verificarRuta(self, codigo):
        encontrado = False
        i = 0
        while not encontrado and i < len(self.__listaRutas):
            if self.__listaRutas[i].getCodigo() == codigo:
                encontrado = True
            else:
                i += 1

        if encontrado:
            if self.__listaRutas[i].getRutaAsignada() is True:
                raise IOError("\nERROR - La ruta elegida ya está asignada para otro camión")
            else:
                return self.__listaRutas[i]
        else:
            raise IndexError("\nERROR - Ruta no encontrada")
        
    def menuElegirRutas(self):
        opcion = int(input('''
Mostrar rutas [1]        Elegir ruta [2]        Salir [0]
Su opción --> '''))
        return opcion

    def elegirRutas(self, camion):
        try:
            opcion = self.menuElegirRutas()
            while opcion != 0:
                if opcion == 1:
                    self.mostrarRutas()
                    
                elif opcion == 2:
                    codigo = int(input("\nIngrese el código de la ruta que desea recorrer: "))
                    ruta = self.verificarRuta(codigo)

                    if ruta:
                        ruta.setRutaAsignada(True)
                        camion.agregarRuta(ruta)

                else:
                    print("\n ERROR - Opción no válida")

                opcion = self.menuElegirRutas()

            if camion.tieneRuta() is True:
                print("\nRegresando al menú...")
            else:
                print("\nERROR - Debe elegir al menos una ruta")
                self.elegirRutas(camion)

        except IndexError as ie:
            print(ie)
            self.elegirRutas(camion)
        except IOError as io:
            print(io)
            self.elegirRutas(camion)