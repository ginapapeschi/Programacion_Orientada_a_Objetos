from GestorLadrillo import GestorLad
from GestorMaterial import GestorMat

def menu_opciones(self):
    op = None
    try:
        op = int(input("""
                                        MENÚ DE OPCIONES
        1) Ingrese el ID del ladrillo para detallar costo y características del material.
        2) Mostrar el costo total de fabricación para cada ladrillo del pedido.
        3) Mostrar detalles de ladrillos.
        0) SALIR DEL MENÚ.
        Su opción -->  """))
    except ValueError:
        pass
    return op

if __name__ == '__main__':
    GL = GestorLad()
    GM = GestorMat()
    GL.leerdatos()
    GM.leerdatos()
    opcion = menu_opciones()
    while opcion != 0:
        if opcion == 1:
                print("\n")
                ID = int(input("Ingrese el ID del ladrillo:"))
                GL.mostrarDatosMateriales(ID)