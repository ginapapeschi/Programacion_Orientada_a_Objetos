import csv
from clasePlanes import Plan
from claseTelefonia import Telefonia
from claseTelevision import Television

class GestorPlanes:
    __listaPlanes: list

    def __init__(self):
        self.__listaPlanes = []

    def agregarPlan(self, unPlan):
        self.__listaPlanes.append(unPlan)
        if isinstance(unPlan, Telefonia):
            print("Plan de telefonía cargado.")
        elif isinstance(unPlan, Television):
            print("Plan de televisión cargado.")

    def cargarCSVPlanes(self):
        archivo = open('planes.csv', encoding='utf-8')
        reader = csv.reader(archivo, delimiter=';')
        next(reader)
        for fila in reader:
            if fila[0] == 'M':
                telefonia = Telefonia(fila[1], int(fila[2]), fila[3], float(fila[4]), fila[5], int(fila[6]))
                self.agregarPlan(telefonia)

            elif fila[0] == 'T':
                television = Television(fila[1], int(fila[2]), fila[3], float(fila[4]), int(fila[5]), int(fila[6]))
                self.agregarPlan(television)

        archivo.close()

    # Inciso 1
    def mostrarPlanPorPosicion(self, pos):
        if pos < 0 or pos >= len(self.__listaPlanes):
            raise IndexError("\nERROR - Posición no válida.")
        
        else:
            plan = self.__listaPlanes[pos]
            if isinstance(plan, Telefonia):
                print(f"El plan almacenado en la posición {pos} es {plan.__class__.__name__}.")
            
            elif isinstance(plan, Television):
                print(f"El plan almacenado en la posición {pos} es Television.")

    # Inciso 2
    def mostrarPlanesPorCobertura(self, cobertura):
        contCobertura = 0
        if cobertura.lower() in ['nacional', 'internacional', 'regional', 'nacional e internacional']:
            for plan in self.__listaPlanes:
                if cobertura.lower() in plan.getCobertura().lower(): # El "in" permite que se detecte el caso de "Nacional e Internacional".
                    print("-------------------------------------")
                    print(plan)
                    contCobertura += 1

            print("-------------------------------------")    
            print(f"\nCantidad de planes con cobertura {cobertura}: {contCobertura}.")

        else:
            print("\nERROR - Cobertura ingresada no válida.")

    # Inciso 3
    def mostrarCompaniasPorCantidad(self, cantCanales):
        encontrado = False
        encabezado = False

        for plan in self.__listaPlanes:
            if isinstance(plan, Television):
                if plan.getCantCanalesInternacionales() >= cantCanales:
                    if not encabezado:
                        encabezado = True
                        print(f"\n --- Compañías con al menos {cantCanales} canales ---")
                    print(f" - {plan.getNomCompania()}")
                    encontrado = True
        
        if not encontrado:
            print(f"\nERROR - No se encontraron compañías con al menos {cantCanales} canales internacionales.")

    def mostrarPlanes(self):
        self.__listaPlanes.sort()
        for plan in self.__listaPlanes:
            print(f"\n----------- PLAN DE {plan.__class__.__name__.upper()} -----------")
            print(plan.mostrarInfoSuper())
            print(f"Importe final: ${plan.getImporteFinal():.2f}")