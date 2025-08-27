from ClaseEdificio import Edificio
import csv

class GestorEdificio:
    __lista_edificio: list

    def __init__(self):
        self.__lista_edificio = []
    
    def agregarEdificio(self, nuevoEdificio):
        self.__lista_edificio.append(nuevoEdificio)

    def cargaEdificio (self):
        archivo = open("EdificioNorte.csv")
        reader = csv.reader (archivo, delimiter = ';')
        xedificio = None    # Ver esto
        for fila in reader:
            if len(fila) == 6:
                xedificio = Edificio(int(fila[0]), fila[1], fila[2], fila[3], int(fila[4]), int(fila[5]))
                self.agregarEdificio(xedificio)
            else:
                id = int(fila[1])
                nom = fila[2]
                nroP = int(fila[3])
                nroD = int(fila[4])
                cantD = int(fila[5])
                cantB = int(fila[6])
                sup = float(fila[7])
                xedificio.agregarDepartamento(id, nom, nroP, nroD, cantD, cantB, sup)
        archivo.close()

    def mostrarPropietarios(self, nomEdi):
        band = True
        i = 0
        while  i < len(self.__lista_edificio) and band:
            if self.__lista_edificio[i].getNombre() == nomEdi:
                band = False
            else:
                i += 1
        if not band:
            self.__lista_edificio[i].mostrarPropietariosDeptos()
        assert band is False

    def mostrarSuperficieEdificio(self, id):
        band = True
        i = 0
        sup: float = 0
        while i < len(self.__lista_edificio) and band:
            if self.__lista_edificio[i].getID() == id:
                sup = self.__lista_edificio[i].calcularSup()        # Siempre poné el subíndice [i] gina la concha de la lora
                band = False
                print("Superficie total cubierta del edificio con ID {} es: {}.".format(id, sup))
            else:
                i += 1
        assert band is False

    def mostrarSuperficieDepto(self, nomProp):
        band = True
        i = 0
        while i < len(self.__lista_edificio) and band:
            supDepto = self.__lista_edificio[i].getSuperficiePorNombre(nomProp)
            if supDepto != -1:
                print(f"La superficie total cubierta del departamento es: {supDepto:.0f}.")
                supTotal = self.__lista_edificio[i].calcularSup()   # Gina pelotuda no te olvidés de los () al llamar a cada método
                supDepto = supDepto * 100 / supTotal
                print(f"El porcentaje que representa del total de la superficie cubierta del edificio es: {supDepto}%.")
                band = False
            else:
                i += 1
        assert band is False
                
    def mostrarCantDeptosCondiciones(self, numPiso):
        band = False
        i = 0
        contador = 0
        while i < len(self.__lista_edificio):
            pisoDepto = self.__lista_edificio[i].getCantByH(numPiso)
            if pisoDepto != -1:
                contador += 1
                band = True
            i += 1
        if band is True:
            print(f"La cantidad de departamentos en el piso {numPiso} con 3 dormitorios y más de un baño son: {contador}.")
        assert band is True