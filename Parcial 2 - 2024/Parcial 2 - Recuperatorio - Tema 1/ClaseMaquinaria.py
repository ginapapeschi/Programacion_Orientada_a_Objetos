from ClaseEquipo import Equipo

class Maquinaria(Equipo):
    __tipoMaq: str
    __peso: int

    def __init__(self, marca, model, a, tipo, pot, cap, tarifa, cant, tipoM, peso):
        super().__init__(marca, model, a, tipo, pot, cap, tarifa, cant)
        self.__tipoMaq = tipoM
        self.__peso = peso

    def getTipoMaq(self):
        return self.__tipoMaq
    
    def getPeso(self):
        return self.__peso
    
    def calcularTarifaAlquiler(self):
        imp = super().getTarifaAlq()
        cantDias= super().getCantDiasAlq()
        if self.getPeso() <= 10:
            imp = imp * cantDias
        elif self.getPeso() > 10:
            imp = imp * cantDias + (cantDias * 20 / 100)
        return imp

    def __str__ (self):
        return f"Marca: {super().getMarca()}\nModelo: {super().getModelo()}\nAño de fabricación: {super().getAnio()}\nTipo de combustible: {super().getTipoCombustible()}\nPotencia: {super().getPotencia()}\nCapacidad de carga: {super().getCapacidadCarga()}"