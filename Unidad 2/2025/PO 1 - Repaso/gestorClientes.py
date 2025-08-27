import csv
from claseClientes import Cliente

class GestorClientes:
    __listaClientes: list

    def __init__(self):
        self.__listaClientes = []

    def agregarCliente(self, unCliente):
        self.__listaClientes.append(unCliente)
        print("Cliente cargado.")

    def cargarCSVClientes(self):
        archivo = open('ClientesAbril2024.csv', encoding='utf-8')
        reader = csv.reader(archivo, delimiter=';')
        band = True
        for fila in reader:
            if band:
                band = False
            else:
                cliente = Cliente(fila[0], fila[1], fila[2], int(fila[3]), float(fila[4]))
                self.agregarCliente(cliente)
        archivo.close()

    # Inciso A
    def actualizarSaldo(self, dni, gestorMov):
        encontrado = False
        i = 0
        while not encontrado and i < len(self.__listaClientes):
            if self.__listaClientes[i].getDNI() == dni:
                encontrado = True
                numTarjeta = self.__listaClientes[i].getNumTarjeta()
                saldoAnterior = self.__listaClientes[i].getSaldoAnterior()
                saldoActual = gestorMov.getSaldoTotalMovimientos(numTarjeta, saldoAnterior)

            else:
                i += 1

        if encontrado:
            print(f"\nListado de movimientos:")
            AyN = self.__listaClientes[i].getApellido() + ' ' + self.__listaClientes[i].getNombre()
            print(f"\nCliente: {AyN:<30}")
            print(f"Número de tarjeta: {numTarjeta:<20}")
            print(f"Saldo anterior: ${saldoAnterior:.2f}")
            gestorMov.mostrarListado(numTarjeta)
            print(f"Saldo actualizado: ${saldoActual:.2f}")
           
        else:
            print("\nNo se encontró el DNI ingresado.")

    # Inciso B
    def mostrarSiTuvoMovimientos(self, numTarjeta, gestorMov):
        encontrado = False
        i = 0
        while not encontrado and i < len(self.__listaClientes):
            if self.__listaClientes[i].getNumTarjeta() == numTarjeta:
                encontrado = True
                tuvo = gestorMov.tuvoMovimientosAbril(numTarjeta)
                AyN = self.__listaClientes[i].getApellido() + ' ' + self.__listaClientes[i].getNombre()
            
            else:
                i += 1

        if encontrado:
            if tuvo == 1:
                print(f"\nEl/la cliente {AyN} tuvo movimientos en abril.")
            else:
                print(f"\nEl/la cliente {AyN} no tuvo movimientos en abril.")
            
        else:
            print("\nNo se encontró el número de tarjeta ingresado.")