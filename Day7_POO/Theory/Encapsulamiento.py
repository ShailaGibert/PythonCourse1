"""
--- ENCAPSULAMIENTO ------
"""


# En Java es una implementación habitual [getters & setters]
# En Python no viene implementado

# Para hacer de un atributo privado, se deben poner __ delante del atributo

class Perro:
    def __init__(self, raza, edad, pelaje):
        self.__raza = raza
        self.__edad = edad
        self.__pelaje = pelaje

    def set_raza(self, raza):
        self.__raza = raza

    def set_edad(self, edad):
        self.__edad = edad

    def set_pelaje(self, pelaje):
        self.__pelaje = pelaje

    def get_raza(self):
        return self.__raza

    def get_edad(self):
        return self.__edad

    def get_pelaje(self):
        return self.__pelaje

    def __str__(self):
        return f"Raza: {self.__raza}, Edad: {self.__edad}, Pelaje: {self.__pelaje}."


perro1 = Perro("Beagle", 10, "Largo")
print(perro1)
print(f"La raza del perro es: {perro1.get_raza()}")
print("Ahora vamos a cambiar la raza con el setter")
perro1.set_raza("Yorkshire")
print(f"La raza del perro ahora es: {perro1.get_raza()}")
print(perro1)
