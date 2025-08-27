import csv
from claseReservas import Reserva

class GestorReserva:
    __listaR: list

    def __init__(self):
        self.__listaR = []
    
    def agregarReserva(self, unaReserva):
        self.__listaR.append(unaReserva)
        print("Reserva cargada.")
    
    def cargarCSVReservas(self):
        archivo = open('Reservas.csv', encoding='utf-8')
        reader = csv.reader(archivo, delimiter=';')
        band = True
        for fila in reader:
            if band:
                band = False
            else:
                reserva = Reserva(int(fila[0]), fila[1], int(fila[2]), fila[3], int(fila[4]), int(fila[5]), float(fila[6]))
                self.agregarReserva(reserva)
        archivo.close()

    # Inciso A
    def tieneReserva(self, numCabaña):
        encontrado = 0
        i = 0
        while encontrado == 0 and i < len(self.__listaR):
            if self.__listaR[i].getNumCabaña()== numCabaña:
                encontrado = 1

            else:
                i += 1

        return encontrado
    
    # Inciso B
    def listadoReservasFecha(self, fecha, gestorCab):
        hay = False
        encabezadoImpreso = False
        print(f"\nReservas para la fecha: {fecha}")
        for reserva in self.__listaR:
            if reserva.getFecha() == fecha:
                if not encabezadoImpreso:
                    print(f"{'Nº de cabaña':<5} | {'Importe diario':<5} | {'Cantidad días':<5} | {'Seña':<10} | {'Importe a cobrar':<10}")
                    encabezadoImpreso = True
                hay = True
                numCabaña = reserva.getNumCabaña()
                importeDiario = gestorCab.getImporteCabaña(numCabaña)
                print(f"{reserva.getNumCabaña():<12} | ", end='')
                print(f"${importeDiario:<13.2f} | ", end='')
                print(f"{reserva.getCantDias():<13} | ", end='')
                print(f"${reserva.getImporte():<5.2f} | ", end='')
                print(f"${reserva.getCantDias() * importeDiario - reserva.getImporte():<15.2f}")
                
        if not hay:
            print("\n- No se registraron reservas para la fecha ingresada.")