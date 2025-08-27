import csv
from claseBeneficiario import Beneficiario

class ManejadorBeneficiario:
    __listaBenef: list

    def __init__(self):
         self.__listaBenef = []

    def agregarBeneficiario(self, unBeneficiario):
        self.__listaBenef.append(unBeneficiario)

    def cargarCSVBeneficiarios(self):
        archivo = open('beneficiarios.csv', encoding='utf-8')
        reader = csv.reader(archivo, delimiter=';')
        band = True
        for fila in reader:
            if band:
                band = False
            else:
                beneficiario = Beneficiario(fila[0], fila[1], fila[2], fila[3], fila[4], int(fila[5]), float(fila[6]), int(fila[7]))
                self.agregarBeneficiario(beneficiario)
                print("Beneficiario cargado.")
        archivo.close()

    # Inciso A
    def informarBeneficiariosBeca(self, IDBeca):
        beneficiarios = []
        cont = 0
        for i in range(len(self.__listaBenef)):
            if self.__listaBenef[i].getIDBeca() == IDBeca:
                NyA = self.__listaBenef[i].getNombre().strip() + ' ' + (self.__listaBenef[i].getApellido().strip())     #El método strip() es para eliminar cualquier espacio en blanco que contenga el string.
                beneficiarios.append(NyA)
                cont += 1
        
        if beneficiarios:
            print("\nBeneficiarios de la beca:")
            for b in beneficiarios:
                print(b)
        else:
            print("\nNo hay beneficiarios para la beca ingresada.")

        return cont
    

    def incisoB(self, dni):
        cont = 0
        NyA = None
        for beneficiario in self.__listaBenef:
            if beneficiario.getDNI() == dni:
                cont += 1
                NyA = beneficiario.getNombre() + ' ' + beneficiario.getApellido()
        
        if NyA:
            if cont > 1:
                print(f"\nEl beneficiario {NyA} tiene más de una beca asignada.")
            else:
                print(f"\nEl beneficiario {NyA} no tiene más de una beca asignada.")
        else:
            print(f"\nNo se encontró un beneficiario con DNI {dni}.")

    def incisoC(self):
        print("\nLista de beneficiarios:")
        self.__listaBenef.sort()
        for beneficiario in self.__listaBenef:
            NyA = beneficiario.getNombre() + ' ' + beneficiario.getApellido()
            print(f"{NyA} - {beneficiario.getSiglaF()}")

    def incisoD(self):
        estudiantes = []
        for beneficiario in self.__listaBenef:
           if beneficiario.getPromedio() > 8 and beneficiario.getIDBeca() != 4:
                estudiantes.append(beneficiario)

        if estudiantes:
            print("\nEstudiantes con promedio mayor a 8 que no poseen beca de ayuda económica:")
            for estudiante in estudiantes:    
                NyA = estudiante.getNombre() + ' ' + estudiante.getApellido()
                print(f"{NyA} - Promedio: {estudiante.getPromedio()}")

        else:
            print("\nNo hay estudiantes con promedio mayor a 8 que no tengan beca de ayuda económica.")


