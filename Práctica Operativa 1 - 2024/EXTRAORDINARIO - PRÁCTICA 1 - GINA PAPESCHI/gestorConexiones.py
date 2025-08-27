from claseConexiones import Conexion
import csv
import numpy as np

class GestorConexion:
    __incremento: int
    __dimension: int
    __cantidad: int
    __lista: np.ndarray
    
    def __init__ (self):
        self.__dimension = 0
        self.__cantidad = 0
        self.__incremento = 1
        self.__lista = np.empty(self.__dimension, dtype=Conexion)
        
    def agregarConexion(self, unaConexion):
        if self.__cantidad == self.__dimension:
            print("Se solicitó espacio de memoria.")
            self.__dimension += self.__incremento
            self.__lista.resize(self.__dimension)
        self.__lista[self.__cantidad] = unaConexion
        self.__cantidad += 1
    
    def leerCSVConexion(self):
        archivo = open("conexiones.csv")
        reader = csv.reader(archivo, delimiter=";")
        next(reader)
        for fila in reader:
            conexion = (Conexion(int(fila[0]), fila[1], fila[2], fila[3], int(fila[4]), int(fila[5])))
            self.agregarConexion(conexion)
        archivo.close()
        print("Conexiones cargadas con éxito.")
        
        
    def calcularTotalHoras(self, idJugador):
        i = 0
        totalHoras = 0
        band = True
        while i < len(self.__lista) and band:
            if self.__lista[i].getIDJugador() == idJugador:
                band = False
                horaInicio = self.__lista[i].getHoraInicio()
                horaFin = self.__lista[i].getHoraFinalizacion()
                totalHoras += horaFin - horaInicio
            i += 1
        return totalHoras
    

    def listadoConexiones(self, dni, gestorGammer):
        idJugador = gestorGammer.buscarDNI(dni)
        if idJugador != -1:
            gestorGammer.mostrarDatosIncisoA(dni)
            print(f"{'Ip de conexión:':^15} {'Juego:':^15} {'Fecha:':^15} {'Hora inicio:':^15} {'Hora fin:':^15}")
            for conexion in self.__lista:
                if conexion.getIDJugador() == idJugador:
                    print(f"{conexion.getDirIP():^15} {conexion.getNombreJuego():^15} {conexion.getFecha():^15} {conexion.getHoraInicio():^15} {conexion.getHoraFinalizacion():^15}")
            print(f"""
Total de horas: {self.calcularTotalHoras(idJugador)} horas
Horas en exceso: {gestorGammer.calcularHorasEnExceso(idJugador, self.calcularTotalHoras(idJugador))} horas 
Importe a facturar: ${round(gestorGammer.calcularImporteAFacturar(idJugador, gestorGammer.calcularHorasEnExceso(idJugador, self.calcularTotalHoras(idJugador))))}""")
        else:
            print("El DNI ingresado no existe.")
            

    def buscarJuego(self, nombreJuego):
        i = 0
        band = False
        while i < len(self.__lista) and band is False:
            if self.__lista[i].getNombreJuego() == nombreJuego:
                band = True
            i += 1
        return band
    

    def buscarDirIP(self, idJugador, nombreJuego):
        dirIP = -1
        i = 0
        band = True
        while i < len(self.__lista) and band:
            if self.__lista[i].getIDJugador() == idJugador and self.__lista[i].getNombreJuego() == nombreJuego:
                band = False
                dirIP = self.__lista[i].getDirIP()
            i += 1
        return dirIP
    
    def juegaSimultaneo(self, id):
        band = False
        self.__lista.sort()
        for conexion in self.__lista:
            i = 0
            j = 0
            if conexion.getIDJugador() == id:
                while i < len(self.__lista) and band is False:
                    j = i+1
                    while j < len(self.__lista):
                        if i != j and self.__lista[i] == self.__lista[j]:
                            band = True
                        j += 1
                    i += 1
        return band

    def ordenarLista(self):
        self.__lista.sort()
        for conexion in self.__lista:
            print("\n")
            print(conexion)