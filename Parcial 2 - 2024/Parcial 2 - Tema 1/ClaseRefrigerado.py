from ClaseProducto import Producto

class Refrigerado(Producto):
    __codigo: str

    def __init__(self, nom, fechaE, fechaV, temp, pais, num, costo, cod):
        super().__init__(nom, fechaE, fechaV, temp, pais, num, costo)
        self.__codigo = cod
    
    def __str__(self):
        return f"\nNombre del producto: {self._Producto__nombre}\nFecha de envasado: {self._Producto__fechaEnv}\nFecha de vencimiento: {self._Producto__fechaVenc}\nTemperatura: {self._Producto__temperatura}\nPaís de origen: {self._Producto__paisOrigen}\nNúmero de lote: {self._Producto__numLote}\nCosto base: ${self._Producto__costo}\nCódigo: {self.__codigo}"    

    def getCodigo(self):
        return self.__codigo
    
    def importeVenta(self):
        fecha_vencimiento = self.getFechaVenc().split('/')
        fecha_actual = "01/06/2024".split('/')  # Suponiendo que la fecha actual es 01/06/2024 para esta implementación.

        anio_vencimiento = int(fecha_vencimiento[2])    # Particiona la fecha en un arreglo de 3 posiciones, tomando la tercera ([2]) como año y la segunda ([1]) como el mes.
        mes_vencimiento = int(fecha_vencimiento[1])

        anio_actual = int(fecha_actual[2])              # Realiza lo mismo con la fecha de vencimiento.
        mes_actual = int(fecha_actual[1])

        # Calcular la diferencia en meses
        meses_diferencia = (anio_vencimiento - anio_actual) * 12 + (mes_vencimiento - mes_actual)

        imp = super().getCosto()
        if meses_diferencia <= 2:
            imp -= imp * 10 / 100
        else: 
            imp += imp * 1 / 100
        return imp