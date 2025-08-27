import csv
from claseBeca import Beca

class ManejadorBeca:
    __listaBeca: list

    def __init__(self):
        self.__listaBeca = []

    def agregarBeca(self, unaBeca):
        self.__listaBeca.append(unaBeca)

    def cargarCSVBecas(self):
        archivo = open('becas.csv', encoding='utf-8')
        reader = csv.reader(archivo, delimiter=';')
        band = True
        for fila in reader:
            if band:
                band = False
            else:
                beca = Beca(int(fila[0]), fila[1], float(fila[2]))
                self.agregarBeca(beca)
                print("Beca cargada.")
        archivo.close()

    def incisoA(self, tipoBeca, mBenef):
        encontrado = False
        i = 0
        impTotal = 0
        becaBienEscrita = None
        while not encontrado and i < len(self.__listaBeca):
            if self.__listaBeca[i].getTipoBeca().lower() == tipoBeca:
                encontrado = True
                cantBeneficiados = mBenef.informarBeneficiariosBeca(i + 1)
                impTotal += self.__listaBeca[i].getImporte() * cantBeneficiados
                becaBienEscrita = self.__listaBeca[i].getTipoBeca()
            else:
                i += 1

        if encontrado:       
            print(f"\nEl importe total que debe disponer la Secretaría para el pago de la beca {becaBienEscrita} es ${impTotal:.2f}")
        else:
            print(f"\nNo se encontró la beca ingresada.")