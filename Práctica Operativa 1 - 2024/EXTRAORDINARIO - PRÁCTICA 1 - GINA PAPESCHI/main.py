from gestorConexiones import GestorConexion
from gestorGammers import GestorGammer

def menu_opciones():
    op = str(input("""
                                                    MENÚ DE OPCIONES
        a) Ingresar DNI de un Gammer y mostrar un listado de las conexiones.
        b) Ingresar nombre de un juego y mostrar información de usuarios que han jugado dicho juego.
        c) Emitir un listado de jugadores con servicio Básico, que se conectan en IP’s distintas, simultáneamente.
        d) Ordenar conexiones y mostrarlas.
        e) Salir del menú.
        Su opción --> """))
    return(op.lower())

if __name__ == "__main__":
    gestorConexion = GestorConexion()
    gestorGammer = GestorGammer()
    gestorConexion.leerCSVConexion()
    gestorGammer.leerCSVGammer()
    opcion = menu_opciones()
    
    while opcion != "e":
        if opcion == "a":
            dniGammer = int(input("\nIngrese DNI: "))
            gestorConexion.listadoConexiones(dniGammer, gestorGammer)
        
        elif opcion == "b":
            nombreJuego = str(input("\nIngrese nombre del juego: "))
            gestorGammer.mostrarJugadores(nombreJuego, gestorConexion)

        elif opcion == "c":
            gestorGammer.listadoServicioBasico(gestorConexion)

        elif opcion == "d":
            gestorConexion.ordenarLista()

        else:
            print("\nERROR - Opción inválida")
            opcion = menu_opciones()

        opcion = menu_opciones()