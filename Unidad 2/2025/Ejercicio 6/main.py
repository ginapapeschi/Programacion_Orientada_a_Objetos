from manejadorAtenciones import ManejadorAtencion
from manejadorPacientes import ManejadorPaciente

def menu():
    print()
    print("MENÚ DE OPCIONES".center(60))
    op = input('''
a) Informar atenciones y el importe a pagar en una fecha dada
b) Informar cantidad de atenciones de un paciente
c) Listado de pacientes sin atención
d) Listar pacientes ordenados
z) SALIR

Su opción --> ''')
    
    return op

if __name__ == '__main__':
    mAtenciones = ManejadorAtencion()
    mPacientes = ManejadorPaciente()
    mAtenciones.cargarCSVAtenciones()
    mPacientes.cargarCSVPacientes()
    opcion = menu().lower()

    while opcion != 'z':
        if opcion == 'a':
            fecha = input("\nIngrese la fecha: ")
            mAtenciones.incisoA(fecha)

        elif opcion == 'b':
            dni = input("\nIngrese el DNI del paciente: ")
            mPacientes.incisoB(dni, mAtenciones)
        
        elif opcion == 'c':
            mPacientes.incisoC(mAtenciones)

        elif opcion == 'd':
            mPacientes.incisoD()

        else:
            print("\nERROR - Opción inválida.")
        
        opcion = menu().lower()