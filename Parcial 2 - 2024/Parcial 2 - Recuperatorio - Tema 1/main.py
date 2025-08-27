from ClaseLista import Lista
from ClaseEquipo import Equipo
from ClaseHerramientas import Herramienta
from ClaseMaquinaria import Maquinaria

def menu():
    op = None
    try:                                                    
        op = int(input("""
                                                                     MENÚ DE OPCIONES
                    1) Cargar productos
                    2) Ingresar posición de la lista a la que se desea acceder para mostrar qué tipo de equipo se encuentra almacenado
                    3) Ingresar año de fabricación para indicar cantidad de herramientas eléctricas fueron fabricados en dicho año
                    4) Mostrar cantidad de equipos de tipo maquinarias pesadas cuya capacidad de cargar es menor o igual a una ingresada
                    5) Mostrar equipos
                    0) SALIR
                    Su opción --> """))
    except ValueError:
        print("\nERROR - Se esperaba un número.\n")
    return op

if __name__ == '__main__':
    opcion = menu()
    gestor = Lista()

    while opcion != 0:
        if opcion == 1:
            print("")
            gestor.cargarEquipo()

        elif opcion == 2:
            try:                                            
                pos = int(input("\nIngrese la posición: "))
                gestor.mostrarEquipoPos(pos-1)
            except ValueError:
                print("\nERROR - Se esperaba un número.")
            except IndexError as e:
                print(e)

        elif opcion == 3:
            try:                                            
                anio = int(input("\nIngrese el año: "))
                gestor.mostrarCantHerramientasFabricadas(anio)
            except ValueError:
                print("\nERROR - Se esperaba un número.")

        elif opcion == 4:
            try:                                            
                capacidad = int(input("\nIngrese la capacidad: "))
                gestor.mostrarCantMaquinariasCapacidad(capacidad)
            except ValueError:
                print("\nERROR - Se esperaba un número.")
        
        elif opcion == 5:
            print("\nLISTA DE EQUIPOS:")
            gestor.mostrarEquipos()

        elif opcion not in range (5):
            print("\nERROR - OPCIÓN INVÁLIDA")
            
        opcion = menu()