"""
---------- CLASES -----------
"""

# Se definen con la palabra class

class PrimeraClasse:
    pass #Clase vacía

primer_objeto_de_clase = PrimeraClasse() #Constructor predefinido vacío

'''
Se pueden asignar atributos
1. Atributos de la clase = existen para todos los objetos de esa clase
2. Atributos de instancia = existen para SÓLO el objeto en el que lo estemos creando
'''


class Pajaro:

    tiene_alas = True #Este es un atributo de la clase. No es necesario añadirlo en el constructor dado que siempre
    #tendrá el mismo valor

    # Indicamos def para crear un constructor
    def __init__(self, color): #Atributos de la clase
        self.color = color #self == this

pajaro1 = Pajaro('negro') #le indicamos el atributo que hemos pasado al constructor

# Si llamamos al objeto, nos saldrá dentro las funcionalidades de la clase y sus atributos
print(pajaro1.color)
