from claseClientes import Cliente
import csv

class GestorCliente:
    __lista: list

    def __init__(self):
        self.__lista = []

    def agregarCliente(self, unCliente):
        self.__lista.append(unCliente)

    def leerCSV(self):
        archivo = open("ClientesFarmaCiudad.csv")
        reader = csv.reader(archivo, delimiter=";")
        next(reader)
        for fila in reader:
            cliente = (Cliente(fila[0], fila[1], int(fila[2]), int(fila[3]), float(fila[4])))
            self.agregarCliente(cliente)
        archivo.close()
        print("\nClientes cargados exitosamente.\n")

    def actualizarSaldo(self, dni, gestorMovimiento):
        i = 0
        band = True
        while i < len(self.__lista) and band:
            if self.__lista[i].getDNICliente() == dni:
                numTarjeta = int(self.__lista[i].getNumTarjeta())
                band = False
            else:
                i += 1

        if band == False:
            print("\n")
            print(f"""                            DATOS DEL CLIENTE:
        Cliente: {self.__lista[i].getNombre()} {self.__lista[i].getApellido()}                    Número de tarjeta: {numTarjeta}
        Saldo anterior: ${round(self.__lista[i].getSaldoAnterior())}
                   """)
        else:
            print(f"\nNo se encontró el DNI ingresado: {dni}")

        saldoActual = gestorMovimiento.buscarNumTarjeta(numTarjeta, self.__lista[i].getSaldoAnterior())
        self.__lista[i].setSaldo(saldoActual)
        print(f"\nSaldo actualizado: ${round(self.__lista[i].getSaldoAnterior())}")

    def buscarNumTarjeta(self, numTarjeta):
        i = 0
        band = True
        while i < len(self.__lista) and band:
            if self.__lista[i].getNumTarjeta() == numTarjeta:
                band = False
                AyN = self.__lista[i].getApellido() + " " + self.__lista[i].getNombre()
            i += 1
        if band is False:
            return AyN