from claseGestorVenta import GestorVenta

def menu():
    op = (input('''             
MENÚ DE OPCIONES
a) Cargar importe
b) Calcular total de facturación
c) Obtener sucursal que más facturó
d) Calcular sucursal con menor facturación semanal
e) Calcular total facturado por la semana
s) SALIR
Su opción --> '''))

    return op

if __name__ == '__main__':
    opcion = menu().lower()
    gestorVenta = GestorVenta()
    
    while opcion != 's':
        if opcion == 'a':
            gestorVenta.cargarSucursal()

        elif opcion == 'b':
            gestorVenta.totalFacturacion()
        
        elif opcion == 'c':
            gestorVenta.maxFacturoPorDia()

        elif opcion == 'd':
            gestorVenta.menorFacturacionSemanal()
        
        elif opcion == 'e':
            gestorVenta.totalFacturadoSemanal()

        else:
            print("ERROR - Opción no válida")
        
        opcion = menu().lower()