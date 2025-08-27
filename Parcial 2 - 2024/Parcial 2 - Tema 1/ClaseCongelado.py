from ClaseProducto import Producto

class Congelado(Producto):
    __nitro: int
    __oxi: int
    __dioxi: int
    __vapor: int
    __metodoCong: str

    def __init__(self, nom, fechaE, fechaV, temp, pais, num, costo, n, o, d, v, metodo):
        super().__init__(nom, fechaE, fechaV, temp, pais, num, costo)
        self.__nitro = n
        self.__oxi = o
        self.__dioxi = d
        self.__vapor = v
        self.__metodoCong = metodo

    def getMetodo(self):
        return self.__metodoCong

    def __str__(self):
        return f"\nNombre del producto: {self._Producto__nombre}\nFecha de envasado: {self._Producto__fechaEnv}\nFecha de vencimiento: {self._Producto__fechaVenc}\nTemperatura: {self._Producto__temperatura}\nPaís de origen: {self._Producto__paisOrigen}\nNúmero de lote: {self._Producto__numLote}\nCosto base: ${self._Producto__costo}\nPorcentaje de nitrógeno: %{self.__nitro}\nPorcentaje de oxígeno: %{self.__oxi}\nPorcentaje de dióxido de carbono: %{self.__dioxi}\nPorcentaje de vapor: %{self.__vapor}\nMétodo de congelamiento: {self.__metodoCong}"

    def importeVenta(self):
        imp = super().getCosto()
        if self.getMetodo() == "mecanico":
            imp += imp * 15 / 100
        elif self.getMetodo() == "criogenico":
            imp += imp * 10 / 100
        return imp