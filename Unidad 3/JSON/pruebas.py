class Persona:
    __nombre: str

    def __init__(self, nombre):
        self.__nombre = nombre

    def __str__(self):
        return f"{self.__nombre}"

p = Persona("Nombre")
print(p.__class__)
print(p.__class__.__name__)

class_ = eval("Persona")
persona = class_("Nombre2")
print(p)
print(persona)


# <class '__main__.Persona'>, __main__ es el nombre del módulo donde se encuentra la clase.
# .__name__ devuelve solo "Persona".