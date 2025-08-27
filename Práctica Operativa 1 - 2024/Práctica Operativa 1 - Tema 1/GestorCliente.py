from ClaseCliente import Cliente
import csv

class GestorCli:
    __listaCli: list

    def __init__(self):
        self.__listaCli = []

    def agregarCliente(self, nuevoCliente):
        self.__listaCli.append(nuevoCliente)

    def leerdatos(self):
        archivo = open('ClientesAbril2024.csv')
        reader = csv.reader(archivo, delimiter = ';')
        band = True
        for fila in reader:
            if band:
                band = False
            else:
                self.agregarCliente(Cliente(fila[0], fila[1], int(fila[2]), int(fila[3]), float(fila[4])))
        archivo.close()

    def buscaDNI(self, xdni):
        i = 0
        pos = -1
        band = True
        while i < len(self.__listaCli) and band:
            if xdni == self.__listaCli[i].getDNI():
                pos = i
                band = False
            else:
                i += 1
        return(pos)

    def actualizarSaldo(self, GM):
        print("\n")
        dni = int(input("Ingrese DNI: "))
        pos = self.buscaDNI(dni)
        if pos != -1:
            AyN = self.__listaCli[pos].getApellido() + " " + self.__listaCli[pos].getNombre()
            Nro_tarjeta = self.__listaCli[pos].getNro_tarjeta()
            saldo = self.__listaCli[pos].getSaldo_anterior() # getea el saldo anterior
            print(f"""
                    Cliente: {AyN}                                      Número de tarjeta: {Nro_tarjeta}
                    Saldo anterior: {saldo}
                    
                    Movimientos:
                    Fecha               Descripción          Importe           Tipo de movimiento""")
            
            for i in range (GM._GestorMov__cantidad): # GM es el parámetro enviado desde el main, GestorMov el nombre de la clase y cantidad es el atributo.
                if Nro_tarjeta == GM._GestorMov__listaMov[i].getNro_tarjeta():    # accede a listaMov para getear el número de la tarjeta y acceder a sus respectivos movimientos
                    fecha = GM._GestorMov__listaMov[i].getFecha()
                    desc = GM._GestorMov__listaMov[i].getDesc()
                    imp = GM._GestorMov__listaMov[i].getImporte()
                    tipo = GM._GestorMov__listaMov[i].getTipoMov()
                    if GM._GestorMov__listaMov[i].getTipoMov() == 'C':
                        saldo += imp  # actualiza el saldo sumándole si es crédito
                    elif GM._GestorMov__listaMov[i].getTipoMov() == 'P':
                        saldo -= imp  # actualiza el saldo restándole si es pago
            print(f"""
                    {fecha}        {desc}          {imp}          {tipo}
                
                    Saldo actualizado: {saldo}""")
        else:
            print("No existe un cliente con ese DNI.")