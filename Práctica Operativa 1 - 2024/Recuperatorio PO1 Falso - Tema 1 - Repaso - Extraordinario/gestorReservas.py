from claseReserva import Reserva
import csv

class GestorReserva:
    __lista = list

    def __init__(self):
        self.__lista = []

    def agregarReserva(self, unaReserva):
        self.__lista.append(unaReserva)

    def leerCSVReserva(self):
        archivo = open("Reservas.csv")
        reader = csv.reader(archivo, delimiter=";")
        next(reader)
        for fila in reader:
            reserva = (Reserva(int(fila[0]), fila[1], int(fila[2]), fila[3], int(fila[4]), int(fila[5]), float(fila[6])))
            self.agregarReserva(reserva)
        archivo.close()
        print("\nReservas cargadas con éxito.")

    def tieneReserva(self, numCabana):
        band = False
        for reserva in self.__lista:
            if reserva.getNumReserva() == numCabana:
                band = True
        return band
    
    def listadoReservados(self, fecha, gestorCabana):
        print(f"\nRESERVAS PARA LA FECHA: {fecha}")
        i = 0
        while i < len(self.__lista):
            if self.__lista[i].getFechaInicio() == fecha:
                print(f"""
Nº de cabaña:   Importe diario:     Cantidad días:      Seña:       Importe a cobrar:
{self.__lista[i].getNumCabanaAsignada()}   ${gestorCabana.importeDiario(round(self.__lista[i].getNumCabanaAsignada()))}     {self.__lista[i].getCantDias()}      ${round(self.__lista[i].getImporteSena())}       ${round(self.__lista[i].getCantDias() * gestorCabana.importeDiario(self.__lista[i].getNumCabanaAsignada()) - self.__lista[i].getImporteSena())}
                      """)
            i += 1