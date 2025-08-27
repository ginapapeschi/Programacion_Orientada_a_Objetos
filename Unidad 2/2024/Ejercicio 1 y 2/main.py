from gestorCajaAhorro import gestorCajaAhorro

if __name__ == "__main__":
    gestorCaja = gestorCajaAhorro()
    gestorCaja.test()
    gestorCaja.mostrarCajas()
    print("\n")
    gestorCaja.extraerImporte(1)
    gestorCaja.depositarImporte(0)
    gestorCaja.verificarCUIL(0)
    print("\n")

""" Lote de Prueba
10
27-46407532-7
Papeschi
Gina
2000
20
20-45213500-1
Perez
Pablo
350.8
30
20-45378619-7
Rodriguez
Juan
1500
"""
