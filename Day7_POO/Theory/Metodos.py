"""
--- MÉTODOS DE UNA CLASE -----
"""

"""
MÉTODOS DE INSTANCIA
"""

# Los métodos de instancia son los que afectan al objeto creado.
# Pueden acceder y modificar los atributos de instancia (de los objetos) desde el que se llaman a los métodos
# Pueden acceder a otros métodos.
# Podemos modificar también los atributos de la clase


print("*" * 20 + "\n CREAR MÉTODOS\n" + "*" * 20)


class Pajaro:

    # Creamos un constructor para la clase
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    # Creamos un método
    def piar(self):
        print("Pio")

    def volar(self, metros):
        print(f"El pájaro ha volado {metros} metros.")

    # Cuando queremos sacar un atributo de un objeto, usamos self que hace referencia al objeto y de ahi el atributo
    def indicar_color(self):
        print(f"El pájaro es de color {self.color}.")

    """
    MÉTODOS DE CLASES
    """

    # Se llaman desde la clase, no desde el objeto. Pajaro.poner_huevos()
    # No pueden modificar los atributos de instancia ni acceder a ellos dado que SE LLAMAN DESDE LA CLASE
    # Sí se pueden modificar y acceder a los atributos de clase

    # Se definen con un decorador

    # Se pueden llamar desde la clase

    @classmethod
    def poner_huevos(cls, cantidad_huevos):
        print(f"El pájaro puso {cantidad_huevos} huevos.")

    """
    MÉTODO ESTÁTICO
    """

    # No se pueden relacionar con objetos, como ocurre con los métodos de clases
    # No acceden ni modifican a ningún tipo de atributos, ni de instancias ni de clases
    # SIRVEN PARA GARANTIZAR QUE NO SE MODIFIQUEN LOS ATRIBUTOS DE LA INSTANCIA NI CLASE
    # Se llaman desde la clase

    # Se definen con un decorador
    @staticmethod
    def mirar():
        print("El pájaro mira y no hace nada mas")


# Instanciamos un objeto de la clase. Una vez instanciado, tendrá los métodos de instancia
pajaro1 = Pajaro("amarillo", "canario")

#Métodos de instancia: [llamados desde el objeto -self-]
pajaro1.piar()
pajaro1.volar(3)
pajaro1.indicar_color()

#Métodos de clase: llamados desde la clase
Pajaro.poner_huevos(3)

#Métodos estáticos: llamados desde la clase
Pajaro.mirar()
