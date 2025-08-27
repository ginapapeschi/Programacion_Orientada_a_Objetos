from ClaseDepartamento import Departamento

class Edificio:
    __id: int
    __nombre: str
    __direccion: str
    __nombreEmpresaConstr: str
    __cant_pisos: int
    __cant_depto: int
    __lista_depto: list        # Lista depto para la composición

    def __init__(self, id, nom, dir, nomE, cantP, cantD):
        self.__id = id
        self.__nombre = nom
        self.__direccion = dir
        self.__nombreEmpresaConstr = nomE
        self.__cant_pisos = cantP
        self.__cant_depto = cantD
        self.__lista_depto = [] # Pa la composición

    def agregarDepartamento(self, id, NyA, numP, numD, cantH, cantB, sup):
        self.__lista_depto.append(Departamento(id, NyA, numP, numD, cantH, cantB, sup))
    
    def mostrarPropietariosDeptos(self):
        print('''
        DEPARTAMENTOS Y SUS PROPIETARIOS:''')
        for departamento in self.__lista_depto:
            print(f"Departamento: {departamento.getID()}, propietario: {departamento.getNyAProp()}")

    def calcularSup(self):
        acum:float = 0
        for departamento in self.__lista_depto:
            acum += departamento.getSupCubierta()
        return acum
    
    def getSuperficiePorNombre(self, nomBuscado):
        i = 0
        band = True
        while i < len(self.__lista_depto) and band:
            if self.__lista_depto[i].getNyAProp() == nomBuscado:
                sup = self.__lista_depto[i].getSupCubierta()
                band = False
            else:
                i += 1
        if band:
            aux = -1
        else:
            aux = sup
        return aux
    
    def getCantByH(self, pisoBuscado):
        i = 0
        contador = 0
        while i < len(self.__lista_depto):
            if self.__lista_depto[i].getNum_piso() == pisoBuscado:
                    if self.__lista_depto[i].getCant_H() == 3 and self.__lista_depto[i].getCant_B() > 1:
                        contador += 1
            i += 1
            print(f"{i}")
        if contador == 0:
            aux = -1
        else:
            aux = contador
        return aux


    def getID(self):
        return self.__id
    
    def getNombre(self):
        return self.__nombre
    
    def getDireccion(self):
        return self.__direccion
    
    def getNomEmpresa(self):
        return self.__nombreEmpresaConstr
    
    def getCant_pisos(self):
        return self.__cant_pisos
    
    def getCant_depto(self):
        return self.__cant_depto