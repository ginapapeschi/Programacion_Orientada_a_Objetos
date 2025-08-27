from gestorMatriculas import GestorMatricula
from gestorEmpleados import GestorEmpleado
from gestorProgramas import GestorPrograma

def menu():
    print()
    print("MENÚ DE OPCIONES".center(70))
    op = int(input('''
1) Informar duración de los programas matriculados
2) Empleados matriculados a un programa
3) Empleados sin matricular
0) SALIR
                                                                         
Su opción --> '''))
    return op

if __name__ == '__main__':
    gestorEmp = GestorEmpleado()
    gestorProg = GestorPrograma()
    gestorMatri = GestorMatricula()
    gestorEmp.cargarCSVEmpleados()
    gestorProg.cargarCSVProgramas()
    gestorMatri.cargarCSVMatriculas(gestorEmp, gestorProg)
    gestorMatri.mostrarMatriculas()
    opcion = menu()

    while opcion != 0:
        if opcion == 1:
            idEmpleado = int(input("\nIngrese el ID del empleado: "))
            gestorMatri.informarDuracion(idEmpleado, gestorEmp)

        elif opcion == 2:
            nomPrograma = input("\nIngrese el nombre del programa: ")
            gestorMatri.informarEmpleadosMatriculados(nomPrograma, gestorProg)

        elif opcion == 3:
            gestorEmp.informarNoMatriculados(gestorMatri)

        else:
            print("\nERROR - Opción inválida.")
        
        opcion = menu()