"""
---- POLIMORFISMO -----
"""


# Objetos de diferentes clases pueden compartir el mismo nombre de métodos y con funcionalidades diferentes

class Vaca:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(f"{self.nombre} dice Muuu")


class Oveja:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(f"{self.nombre} dice Beee")


# Instanciamos los objetos de clase
vaca1 = Vaca("Aurora")
oveja1 = Oveja("Shaun")

# Si llamamos a cada método de instancia de cada objeto, nos llamará al método de su clase
vaca1.hablar()
oveja1.hablar()

# Creamos una lista de objetos diferentes
lista_animales = [vaca1, oveja1]
# Gracias al polimorfismo, nos permite con una iteración, llamar a los métodos que se llaman iguales pero que
# tienen funcionalidades diferentes
for animal in lista_animales:
    animal.hablar()


# Creamos una función
def animal_habla(animal):
    animal.hablar()


for animal in lista_animales:
    animal_habla(animal)
