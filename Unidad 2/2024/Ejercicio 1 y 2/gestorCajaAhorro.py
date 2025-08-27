from claseCajaAhorro import CajaDeAhorro

class gestorCajaAhorro:
    __lista: list

    def __init__(self):
        self.__lista = []

    def agregar(self, unaCaja):
        self.__lista.append(unaCaja)
    
    def test(self):
        for i in range(3):
            nroCuenta = (input(f"\nIngrese número de cuenta de la caja {i+1}: " ))
            cuil = (input("Ingrese número de CUIL: "))
            apellido = (input("Ingrese apellido: "))
            nombre = (input("Ingrese nombre: "))
            saldo = float(input("Ingrese saldo: $"))
            self.agregar(CajaDeAhorro(nroCuenta, cuil, apellido, nombre, saldo))

    def mostrarCajas(self):
        print("\n" + "LISTA DE CAJAS:".center(100))
        for caja in self.__lista:
            print(caja)

    def extraerImporte(self, pos):
        extraccion = self.__lista[pos].extraer(100)
        if extraccion == -1:
            print("\nSaldo insuficiente. No se puede llevar a cabo la operación.")

    def depositarImporte(self, pos):
        self.__lista[pos].depositar(200)
    
    def verificarCUIL(self, pos):
        #self.__lista[pos].validarCUIL(self.__lista[pos].getCUIL())
        self.__lista[pos].validar_cuil()