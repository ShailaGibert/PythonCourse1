"""
----- HERENCIA ------
"""


# Se trata de herencia cuando una clase [hija] hereda de una clase [clase padre]
# Por ejemplo, de ANIMAL [clase padre], heredan las clases MAMÍFERO, RÉPTIL
# La herencia es una abstracción para evitar la repetición de código

class Animal:
    vivo = True

    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    @staticmethod
    def nacer():
        print("Este animal ha nacido")

    def hablar(self):
        print("Este animal emite un sonido")


"""
HERENCIA EXTENDIDA
"""


# La clase hija no solo puede tener atributos heredados, sino también los suyos propios
# La clase hija puede tener los métodos heredados [sin modificar]
# La clase hija también puede tener los métodos modificados [métodos heredados modificados]
# La clase hija puede tener métodos propios

# Al pasar el nombre de la clase como parámetro, ya se indica la herencia
class Pajaro(Animal):

    # Para crear atributos de instancia nuevos, no heredados, será crear un constructor para la clase
    def __init__(self, edad, color, altura_vuelo):
        self.edad = edad
        self.color = color
        # Los atributos heredados pueden ser sutituidos por super().__init__(atributos heredados)
        self.altura_vuelo = altura_vuelo

    def __int__(self, edad, color, altura_vuelo, nombre):
        super().__init__(edad, color)
        self.altura_vuelo = altura_vuelo
        self.nombre = nombre

    # Método heredado modificado: coge un método existente en la clase padre y lo sobrescribe
    def hablar(self):
        print("Pío")

    # Métodos propios: métodos que no existen en la clase padre
    def volar(self, metros):
        print(f"El pájaro ha volado {metros} metros.")


class Perro(Animal):
    pass


# Para saber de qué clase está heredando
print("\n" + "*" * 10 + "\nUsando Pajaro.__base__ para saber de qué clase hereda")
print(Pajaro.__base__)

# Para saber a qué clases está heredando
print("\n" + "*" * 10 + "\nusando Animal.__subclasses__ para saber a qué clases hereda")
print(Animal.__subclasses__())

# Al heredar Pajaro de la clase Animal, podemos hacer lo siguiente
Pajaro.nacer()  # nacer es un método definido en la clase Animal

# Al instanciar un objeto de una clase hija, al heredar los atributos de instancia, hereda el tipo de constructor
# Al crear un constructor propio para la clase Pajaro, tendremos que añadirle tambien los atributos añadidos
pajaro1 = Pajaro(1, "Amarillo", 30)
perro1 = Perro(5, "atigrado")

# También hereda los atributos de clase
print("\n" + "*" * 10 + "\nAtributos de clase heredados")
print(Pajaro.vivo)
print(Perro.vivo)

"""
HERENCIA MÚLTIPLE
"""


# A tener en cuenta:
# En caso de que una clase herede de varias y tengan el mismo método, irá en el orden de herencia.
# Por ejemplo:

class Padre:
    def hablar(self):
        print("Hola")


class Madre:
    def hablar(self):
        print("Hola, soy la mamá")


class Hijo(Padre, Madre):
    pass


hijo1 = Hijo()

# Al heredar primero de padre (al crear la clase indicamos [Padre, Madre], en este orden), hará uso del método de Padre
hijo1.hablar()


class Nieto(Hijo):
    pass


# Para conocer el orden en el que se buscarán los métodos que se llamen usamos:
print("\n" + "*" * 10 + "Orden de herencia en herencia múltiple, uso de __mro__")
nieto1 = Nieto()
print(Nieto.__mro__)
