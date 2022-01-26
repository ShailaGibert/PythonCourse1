"""
---- MÓDULO COLLECTIONS----
"""
# El módulo ya viene integrado en las librerías de pyhton, solo deberemos importar el módulo
from collections import Counter, defaultdict, namedtuple

"""
--- COUNTER ---
"""
# Creamos lista

lista_numeros = [1, 2, 43, 5, 3, 6, 7, 4, 3, 6, 7, 4, 4]

# Queremos contar la cantidad de veces que cada número aparece en la lista
print(Counter(lista_numeros))

# También podemos contar la cantidad de veces que aparece un string
frase = "Al pan pan y al vino vino"
print(Counter(frase.split()))

# Si creamos un objeto del tipo Counter, tendremos varios métodos disponibles
lista = Counter([1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 34, 5, 5, 55, 5])

# Nos indica la cantidad de veces que aparece un valor por tuplas
print(lista.most_common())

"""
--- DEFAULTDICT ---
"""
# Creamos un diccionario del tipo default dic
# en caso de que se llame a una clave del diccionario que no existe, se le pasará como valor 'nada'
mi_diccionario = defaultdict(lambda: 'nada')

# Ahora creamos las claves dentro del diccionario
mi_diccionario["uno"] = "verde"

# Si queremos entonces llamar a una clave del diccionario del defaultdic que no existe, nos mostrará nada
print(mi_diccionario["dos"])

"""
--- NAMEDTUPLE ---
"""

# Tupla con nombres
# Esto nos permite llamar al valor de una posición en una tupla a través de su nombre

# Creamos la named tuple que referencia a una clase
Persona = namedtuple('Persona', ['nombre', 'altura', 'peso'])

persona1 = Persona("Shaila", 1.56, 60)

# Podremos sacar la información a través del nombre del índice
print(persona1.nombre)
# Y también a través de la forma tradicional
print(persona1[0])
