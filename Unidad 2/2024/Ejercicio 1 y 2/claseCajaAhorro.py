class CajaDeAhorro:
    __nroCuenta: str
    __cuil: str
    __apellido: str
    __nombre: str
    __saldo: float

    def __init__(self, nrocta, cuil, ap, nom, sal):
        self.__nroCuenta = nrocta
        self.__cuil = cuil
        self.__apellido = ap
        self.__nombre = nom
        self.__saldo = sal

    def __str__(self):
        return "\n" + f"Número de cuenta: {self.__nroCuenta}" + "\n" + f"CUIL: {self.__cuil}" + "\n" + f"Apellido y Nombre: {self.__apellido} {self.__nombre}" + "\n" + f"Saldo: ${self.__saldo:.2f}"

    def getCUIL(self):
        return self.__cuil

    def extraer(self, imp):
        if self.__saldo >= imp:
            self.__saldo -= imp
            print(f"EXTRACCIÓN - Nuevo saldo de la cuenta {self.__nroCuenta}: ${self.__saldo:.2f}")
        else:
            return -1

    def depositar(self, imp):
        if imp > 0:
            self.__saldo += imp
            print(f"DEPÓSITO - Nuevo saldo de la cuenta {self.__nroCuenta}: ${self.__saldo:.2f}")
        else:
            print("\nERROR - El importe ingresado no es válido.")

    def validar_cuil(self):
            """Metodo para consultar la validez del CUIL"""
            # Esta validacion no es perfecta. Si ingresamos un CUIL en el que originalmente XY era 20/27,
            # como 23; no sera capaz de detectar el error.
            lista=[]
            indice=(0,1,3,4,5,6,7,8,9,10) #Esta tupla contiene los indices de los digitos con los cuales se hara el producto
            constante=(5,4,3,2,7,6,5,4,3,2) #Esta tupla contiene las constantes que multiplicaran a los digitos
            acum=0
            for i in range(len(self.__cuil)-3): #El -3 se debe a los dos guiones(-) y al digito z; los cuales no se tienen en cuenta para realziar la operacion
                lista.append(int(self.__cuil[indice[i]])*constante[i])

            for i in lista:
                acum+=i
            p1=acum//11
            p2=acum-(p1*11)
            if p2==0:
                if self.__cuil[12]!='0':
                    print('CUIL erroneo. El digito de verificacion deberia ser 0')
                    return False
                else:
                    print('El CUIL es valido')
                    return True
            #Este bloque detecta CUILs cuyos digitos XY deberian ser 23, pues son repetidos
            elif p2==1:
                if self.__cuil[0:2]=='20':
                    if self.__cuil[12]!='9':
                        print('CUIL invalido. Los digitos XY deberian tomar el valor 23, y Z el 9')
                    else:
                        print('CUIL invalido. Los digitos XY deberian tomar el valor 23')
                    return False
                elif self.__cuil[0:2]=='27':
                    if self.__cuil[12]!='4':
                        print('CUIL invalido. Los digitos XY deberian tomar el valor 23, y Z el 4')
                    else:
                        print('CUIL invalido. Los digitos XY deberian tomar el valor 23')
                    return False
            else:
                band=False
                valido=('4','9')
                if self.__cuil[0:2]=='23':
                    if (self.__cuil[12] in valido)is False:
                        print('CUIL invalido. Su digito de verificacion deberia ser 4 o 9')
                        return False
                    else:
                        band=True
                else:
                    z=11-p2
                    if int(self.__cuil[12])!=z:
                        print('CUIL invalido. Z deberia tomar el valor ',z)
                        return False
                    else:
                        band=True
                if band is True:
                    print(f'\nCUIL válido: {self.__cuil}')
                    return True

        
"""
    def validarCUIL(self, cuil):
        arreglo = cuil.split("-")
        print(f"\nArreglo: {arreglo}")
        dni = arreglo[1]
        print(f"\nDNI: {dni}")

        band = True
        if arreglo[0] == "20":
            print("\nEl CUIL ingresado pertenece a un hombre.")
        elif arreglo[0] == "27":
            print("\nEl CUIL ingresado pertenece a una mujer.")
        elif arreglo[0] == "30":
            print("\nEl CUIL ingreado pertenece a una empresa.")
        else:
            band = False
        
        if not band:
            print("\nERROR - El CUIL ingresado no es válido.")
        else:
            sum = 0
            aux = 0
            resto = 0
            z = 0
            digitos = arreglo[0] + dni
            print(f"\nDIGITO = {digitos}")
            for digito in digitos:
                sum += 1 * int(digito)
                print(f"\nSumador: {sum}")
            aux = sum // 11
            print(f"\nAux: {aux}")
            resto = sum - (aux * 11)
            print(f"\nResto: {resto}")
        
            if resto == 0:
                z = 0
                print(f"\nDígito Z es {z}")
            elif resto == 1:
                if arreglo[0] == "20":
                    z = 9
                    arreglo[0] = 23
                    print(f"\nDígito de verificación Z es: {z}.")
                elif arreglo[0] == "27":
                    z = 4
                    arreglo[0] = 23
                    print(f"\nDígito de verificación Z es: {z}.")
            else:
                z = 11 - resto 
                print(f"\nDígito de verificación Z es: {z}.")

            cuil_verificado = str("-".join((arreglo[0], dni, str(z))))
            print(f"\nCUIL verificado: {cuil_verificado}")
            if cuil == cuil_verificado:
                print("\nVERIFICACIÓN DE CUIL EXITOSA")
"""