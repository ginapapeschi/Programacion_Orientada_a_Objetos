class Conexion:
    __idJugador: int
    __dirIP: str
    __nombreJuego: str
    __fecha: str
    __horaInicio: int
    __horaFinalizacion: int
    
    def __init__ (self, id, dir, nom, fecha, horaI, horaF):
        self.__idJugador = id
        self.__dirIP = dir
        self.__nombreJuego = nom
        self.__fecha = fecha
        self.__horaInicio = horaI
        self.__horaFinalizacion = horaF

    def __str__(self):
        return f"ID Jugador: {self.__idJugador}\nFecha: {self.__fecha}\nHora de inicio: {self.__horaInicio}\nDirección de IP: {self.__dirIP}"

    def __eq__(self, otro):
        return (self.__idJugador, self.__fecha, self.__horaInicio, self.__dirIP) == (otro.getIDJugador(), otro.getFecha(), otro.getHoraInicio(), otro.getDirIP())
        
    def __lt__(self, otro):
        return (self.__idJugador, self.__fecha, self.__horaInicio, self.__dirIP) < (otro.getIDJugador(), otro.getFecha(), otro.getHoraInicio(), otro.getDirIP())
        
    def getIDJugador(self):
        return self.__idJugador
    
    def getDirIP(self):
        return self.__dirIP
    
    def getNombreJuego(self):
        return self.__nombreJuego
    
    def getFecha(self):
        return self.__fecha
    
    def getHoraInicio(self):
        return self.__horaInicio
    
    def getHoraFinalizacion(self):
        return self.__horaFinalizacion