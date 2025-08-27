import numpy as np

class GestorVenta:
    __arreglo: np.ndarray

    def __init__(self):
       self.__arreglo = np.zeros((5, 7), dtype=float)

    ''' Otra forma de crear un arreglo bidimensional en Python usando listas.
class GestorVenta:
    __venta = []
    __cantfarm = 5  # Número de sucursales
    __cantdias = 7  # Días de la semana

    def __init__(self):
        for i in range(self.__cantfarm):
            self.__venta.append([0] * self.__cantdias)
    '''

    # Inciso a)
    def cargarSucursal(self):
        dia = int(input("\nIngrese el día de la semana (1-7): "))
        if dia > 7 or dia < 1:
            print("\nERROR - Día fuera de rango.")
        else:
            numSuc = int(input("Ingrese el número de la sucursal (1-5): "))
            if numSuc < 1 or numSuc > 5:
                print("\nERROR - Sucursal fuera de rango.")
            else:
                imp = float(input("Ingrese el importe de la factura: "))
                if imp < 0:
                    print("\nERROR - Importe no válido.")
                else:
                    self.__arreglo[numSuc-1][dia-1] += imp
                    print(f"\nPara el día {dia}, sucursal {numSuc}, se cargó el importe de ${imp:.2f}.")
                    print(f"Importe total: ${self.__arreglo[numSuc-1][dia-1]:.2f}")

    # Inciso b)
    def totalFacturacion(self):
        numSuc = int(input("\nIngrese el número de la sucursal (1-5): "))
        if numSuc < 1 or numSuc > 5:
            print("\nERROR - Sucursal fuera de rango.")
        else:
            totalF = 0
            for j in range(7):
                totalF += self.__arreglo[numSuc-1][j]
            print(f"Total de facturación de la sucursal {numSuc}: ${totalF:.2f}.")

    # Dato adicional (por si en algún momento te interesa optimizar o acortar): podrías usar np.sum(self.__arreglo[numSuc - 1]) para que lo sume todo de una.

    # Inciso c)
    def maxFacturoPorDia(self):
        dia = int(input("\nIngrese el día de la semana (1-7): "))
        if dia > 7 or dia < 1:
            print("\nERROR - Día fuera de rango.")
        else:
            max = 0
            for i in range(5):
                if self.__arreglo[i][dia-1] > max:
                    max = self.__arreglo[i][dia-1]
                    numSuc = i
            if max != 0:
                print(f"\nNúmero de la sucursal que más facturó el día {dia}: {numSuc+1}.")
            else:
                print(f"\nNo hay sucursal con mayor facturación en el día {dia}.")

    # Inciso d)
    def menorFacturacionSemanal(self):
        min = 999999999
        sucMin = []
        for i in range(5):
            imp = 0
            for j in range(7):
                imp += self.__arreglo[i][j] 
            if imp < min:
                min = imp
                sucMin = [i]
            elif imp == min:
                sucMin.append(i)

        if len(sucMin) == 1:
            print(f"\nLa sucursal con menor facturación durante toda la semana es la sucursal {sucMin[0] + 1}, con un importe total de ${min:.2f}.")

        elif len(sucMin) > 1:
            sucursales = ""
            for i in range(len(sucMin)):
                sucursales += f"{sucMin[i] + 1}" # Añadir la sucursal
                if i < len(sucMin) - 1:          # Si no es la última sucursal
                    sucursales += ", "           # Añadir una coma entre las sucursales
            print(f"\nLas sucursales con menor facturación son: {sucursales}, con un importe total de ${min:.2f}.")

        else:
            print("\nNo se pudo determinar la sucursal con menor facturación semanal.")

    # Inciso e
    def totalFacturadoSemanal(self):
        total = 0
        for i in range(5):
            for j in range(7):
                total += self.__arreglo[i][j]
        print(f"\nEl total facturado por todas las sucursales en toda la semana es: ${total:.2f}.")