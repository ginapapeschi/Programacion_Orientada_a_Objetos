from manejadorBecas import ManejadorBeca
from manejadorBeneficiarios import ManejadorBeneficiario

def menu():
    print()
    print("MENÚ DE OPCIONES".center(60))
    op = input('''
a) Informar beneficiarios de una beca e importe total
b) Informar si un beneficiario tiene más de una beca
c) Listar beneficiarios
d) Listar estudiantes con promedio mayor a 8 que no poseen beca
z) SALIR
               
Su opción --> ''')
    
    return op

if __name__ == '__main__':
    mBeca = ManejadorBeca()
    mBenef = ManejadorBeneficiario()
    mBeca.cargarCSVBecas()
    mBenef.cargarCSVBeneficiarios()
    opcion = menu().lower()

    while opcion != 'z':
        if opcion == 'a':
            tipoBeca = input("\nIngrese el tipo de beca: ").lower()
            mBeca.incisoA(tipoBeca, mBenef)

        elif opcion == 'b':
            dni = input("\nIngrese el DNI del beneficiario: ")
            mBenef.incisoB(dni)

        elif opcion == 'c':
            mBenef.incisoC()

        elif opcion == 'd':
            mBenef.incisoD()

        else:
            print("\nERROR - Opción inválida")
    
        opcion = menu().lower()