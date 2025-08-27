from claseColeccion import Lista

def mostrarPacientes(listaPacientes):
    for paciente in listaPacientes:
        print()
        print(paciente)
    
def menu():
    print()
    print("MENÚ DE OPCIONES".center(70))
    op = input('''
a) Insertar objetos al final de la colección
b) Pacientes hospitalizados con neumonía y pacientes ambulatorios
c) Mostrar importe cobrado por la clínica
d) Indicar paciente por posición
e) Cambiar valor de consulta
z) SALIR
Su opción --> ''')
    return op

if __name__ == '__main__':
    lista = Lista()
    opcion = menu().lower()

    while opcion != 'z':
        if opcion == 'a':
            lista.cargarCSVPacientes()
            print()
            mostrarPacientes(lista)
            
        elif opcion == 'b':
            lista.contarPacientesConNeumoniaYAmbulatorios()

        elif opcion == 'c':
            lista.mostrarImporteCobrado()

        elif opcion == 'd':
            try:
                posicion = int(input("\nIngrese la posición: "))
                lista.indicarPacientePorPosicion(posicion)

            except IndexError as i:
                print(i)
            except ValueError:
                print("\nERROR - Se esperaba un entero")

        elif opcion == 'e':
            valorConsulta = float(input("\nIngrese el nuevo valor: "))
            lista.cambiarValorConsulta(valorConsulta)

        else:
            print("\nERROR - Opción no válida")

        opcion = menu().lower()

    print("\nPrograma finalizado")
