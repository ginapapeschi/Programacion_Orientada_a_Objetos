from ManejadorCarrera import manejadorCarrera
from ManejadorFacultad import manejadorFacultad

def menu():
    print()
    print("MENÚ DE OPCIONES".center(60))
    op = input('''
a) Cargar CSV de Carreras
b) Cargar CSV de Facultades
c) Mostrar facultad donde se dicta una carrera
d) Mostrar cantidad de carreras que se dictan en cada facultad
e) Listar carreras en orden alfabético
z) SALIR

Su opción --> ''')

    return op

if __name__ == '__main__':
    manejadorC = manejadorCarrera()
    manejadorF = manejadorFacultad()
    opcion = menu().lower()

    while opcion != 'z':
        if opcion == 'a':
            manejadorC.cargarCSVCarrera()
            print("\nCarreras cargadas exitosamente.")

        elif opcion == 'b':
            manejadorF.cargarCSVFacultad()
            print("\nFacultades cargadas exitosamente.")

        elif opcion == 'c':
            nombreCarrera = input("\nIngrese el nombre de la carrera: ")
            manejadorC.incisoC(nombreCarrera, manejadorF)

        elif opcion == 'd':
            manejadorF.calcularTotalCarreras(manejadorC)

        elif opcion == 'e':
            nombreFacultad = input("\nIngrese el nombre de la facultad: ")
            manejadorF.listarCarreras(nombreFacultad, manejadorC)

        else:
            print("\nERROR - Opción inválida.")

        opcion = menu().lower()