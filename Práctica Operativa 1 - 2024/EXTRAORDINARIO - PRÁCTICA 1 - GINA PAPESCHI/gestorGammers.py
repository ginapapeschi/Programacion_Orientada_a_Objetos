from claseGammers import Gammer
import csv

class GestorGammer:
    __lista: list
    
    def __init__(self):
        self.__lista = []
        
    def agregarGammer(self, unGammer):
        self.__lista.append(unGammer)
        
    def leerCSVGammer(self):
        archivo = open("gammers.csv")
        reader = csv.reader(archivo, delimiter=";")
        next(reader)
        for fila in reader:
            gammer = (Gammer(int(fila[0]), int(fila[1]), fila[2], fila[3], fila[4], fila[5], float(fila[6]), int(fila[7])))
            self.agregarGammer(gammer)
        archivo.close()
        print("Gammers cargados con éxito.")
        
    def buscarDNI(self, dni):
        i = 0
        idJugador = -1
        band = True
        while i < len(self.__lista) and band:
            if self.__lista[i].getDNI() == dni:
                band = False
                idJugador = self.__lista[i].getIDJugador()
            i += 1
        return int(idJugador)
            

    def mostrarDatosIncisoA(self, dni):
        for gammer in self.__lista:
            if gammer.getDNI() == dni:
                print("""\n                       LISTADO DE CONEXIONES:""")
                print(f"{'DNI:'} {gammer.getDNI():<15} {'Nombre y apellido:'} {gammer.getNombre()} {gammer.getApellido()}")
                print(f"{'Alias:'} {gammer.getAlias():<15} {'Plan:'} {gammer.getPlan():<15} {'Importe base:':<13} ${round(gammer.getImporteBase()):<15}")

    def calcularHorasEnExceso(self, idJugador, totalHoras):
        i = 0
        band = True
        while i < len(self.__lista) and band:
            if self.__lista[i].getIDJugador() == idJugador:
                band = False
                if self.__lista[i].getPlan() == 'Basico' and totalHoras > 12:
                    totalHoras -= 12
                elif self.__lista[i].getPlan() == 'Completo' and totalHoras > 20:
                    totalHoras -= 20
                elif self.__lista[i].getPlan() == 'Extendido' and totalHoras > 36:
                    totalHoras -= 36
                else:
                    totalHoras = 0
            i += 1
        return totalHoras
    

    def calcularImporteAFacturar(self, idJugador, horasEnExceso):
        i = 0
        band = True
        while i < len(self.__lista) and band:
            if self.__lista[i].getIDJugador() == idJugador:
                band = False
                if self.__lista[i].getPlan() == 'Basico':
                    porcentaje = 0.25
                elif self.__lista[i].getPlan() == 'Completo':
                    porcentaje = 0.30
                elif self.__lista[i].getPlan() == 'Extendido':
                    porcentaje = 0.40
                else:
                    porcentaje = 0
            i += 1
        importeExceso = self.__lista[i].getImporteBase() * porcentaje * horasEnExceso
        importeTotal = self.__lista[i].getImporteBase() + importeExceso
        return importeTotal
    
    
    def mostrarJugadores(self, nombreJuego, gestorConexion):
        band = gestorConexion.buscarJuego(nombreJuego)
        if band:
            print(f"\nLISTA DE JUGADORES QUE JUEGAN {nombreJuego.upper()}:")
            for jugador in self.__lista:
                id = jugador.getIDJugador()
                ip = gestorConexion.buscarDirIP(id, nombreJuego)
                if ip != -1:
                    print(f"""\nDirección de IP: {ip}
Nombre y apellido: {jugador.getNombre()} {jugador.getApellido()}
Alias: {jugador.getAlias()}
Tipo de plan: {jugador.getPlan()}""")
        else:
            print("El juego ingresado no existe.")
            return
        
    def listadoServicioBasico(self, gestorConexion):
        print("\nLISTADO DE JUGADORES CON SERVICIO BÁSICO:")
        for gammer in self.__lista:
            if gammer.getPlan() == "Basico":
                id = gammer.getIDJugador()
                band = gestorConexion.juegaSimultaneo(id)
                if band:
                    print("\n")
                    print(gammer)
