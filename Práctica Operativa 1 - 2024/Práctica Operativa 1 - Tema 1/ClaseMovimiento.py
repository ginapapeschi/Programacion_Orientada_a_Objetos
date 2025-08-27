class Movimiento:
    __nro_tarjeta: int
    __fecha: str
    __descripcion: str
    __tipo_mov: str
    __importe: float

    def __init__(self, nro_t, date, desc, tipo, imp):
        self.__nro_tarjeta = nro_t
        self.__fecha = date
        self.__descripcion = desc
        self.__tipo_mov = tipo
        self.__importe = imp

    def __lt__(self, otro):
        return self.__nro_tarjeta < otro.getNro_tarjeta()
    
    def __str__(self):
        return (f"""
                Número de tarjeta: {self.__nro_tarjeta}
                Fecha: {self.__fecha}
                Descripción: {self.__descripcion}
                Tipo de movimiento:{self.__tipo_mov}
                Importe:{self.__importe}""")

    def getNro_tarjeta(self):
        return self.__nro_tarjeta
    
    def getFecha(self):
        return self.__fecha
    
    def getDesc(self):
        return self.__descripcion
    
    def getTipoMov(self):
        return self.__tipo_mov
    
    def getImporte(self):
        return self.__importe