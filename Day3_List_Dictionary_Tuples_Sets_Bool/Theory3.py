"""
We'll talk about all the types od variables not seen in the other classes [list, tuple, dictionary, set and bool]
"""

"""
---------- INDEX -------------
"""

# Los índices van de 0 a lenght
# También se puede medir al revés. EJ.: [H, o, l, a] = [0, -3, -2, -1]
# Los str tambien son listas

texto = "Holaaaa"
print(texto.index('a'))  # Busca la primera coincidencia y para
print(texto[3])
print(texto[-1])
print(texto.rindex('a'))  # Busca de derecha a izquierda, encuentra la primera coincidencia y para
print(texto.index("Hola"))

"""
----------- SLICING -------------
"""

# Slicing = substraer un string de una string

abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(abecedario[2:])  # Slicing hasta el final
print(abecedario[2:22])  # Incluye el inicio pero excluye el final
print(abecedario[2::2])  # Realiza el slicing salteado de 2 en 2, segun el numero que se indica en el segun argumento
print(abecedario[::-1])  # Slicing inverso
print(abecedario[::1])

"""
-------------- STRING FUNCTIONALITIES --------------
"""
# Lower = upper inverso
print(abecedario.lower())
print(abecedario[::-1].lower())  # Se puede usar el indice y el slicing

# Upper = objecto.toUpperCase()
print(texto.upper())

# Split =  separar el string en elementos y lo almacena en una lista
print(type(abecedario.split()))  ##Slices where the space is
print(abecedario.split('C'))  # Splits where c is and deletes it
print(abecedario.split('DEFG'))

# Join = joins strings using the string you match it with between them
print(abecedario.join([texto, "segunda frase"]))
print(" ".join(["Primera frase seguida de", abecedario, texto]))

# Find = finds str. If not founded, output -1
print("Esto es una prueba".find("z"))

# Replace = replaces first argument for second argument given
print("AAAAAAAAaaaaaaaBBBBBbbbbbbbb".replace("a", "x"))
print("AAAAAAAAaaaaaaaBBBBBbbbbbbbb".replace("AAAAAAAA", "x"))

# in = checks if the str is inside a string and returns bool
# CASE SENSITIVE
print("prueba" in texto)
print("A" in texto)
print("A" not in texto)

# len
print(len(texto))
print(len(abecedario))
print((len(texto + abecedario + "OOOO")))

"""
-------------- LIST FUNCTIONALITIES --------------
"""
# Can be from different types
lista = ['a', 0, 0.45]
print(lista)
print(len(lista))
print(f"{lista[0]} {lista.index(0)}")

##Apend: add item to the list. Returns nothing
lista.append("Ulimo elemento")
print(lista)

##Pop: deletes the last item inserted in the list or the one with the index you indicate. Returns the element deleted
lista.pop()
print(lista)
print(lista.pop(0))
print(lista)

##Sort: orders an array. Returns nothing
lista.append(4)
lista.append(3)
print(lista)
lista.sort()
print(lista)

##Reverse: orders an array in the other way aroung
lista.reverse()
print(lista)

lista.clear()
print(lista)

"""
-------------- DICTIONARY --------------
"""

##En los diccionarios no importa el orden, sino la relacion entre la definición y su palabra clave
customer = {'name' : 'Shaila', 'surname': 'Gibert', 'age': 21, 'height' : 156, 'nationality': ['Spanish', 'Chinese']}
print(customer['name'])

##Modifying value from keys
customer['name'] = 'Karen'
customer['edad'] = 36

##Adding a new key in the dictionary
customer['relationship'] = 'single'
print(customer)

##Print only keys
print(customer.keys())

##Print only values
print(customer.values())

dic = {'c1' : ['a', 'b', 'c'], 'c2' : ['d', 'e', 'f']}
print(dic['c2'][1].upper())

"""
-------------- TUPLES --------------
"""

##They are immutable : cannot change the value in it
tuple = ('Shaila', 21, 'Gibert', 1.56)

tuple_de_numeros = (2.2, -3, -4)

#They can be casted
tuple = list(tuple)

#You can assign each value from the tuple/list/dictionary in variables
name, age, surname, height = tuple
print(name, age, surname, height)

##Count: how many times a value appears
print(tuple.count('Shaila'))
print(tuple.count('a'))

"""
-------------- SETS --------------
"""

##IMPORTANT:
#1. The values are not ordered as in a list or tuple
#2. It only contains unique values. If you try to insert duplicated values, Python will discart them

set = {1, 2, 3, 4, 5}
print(set)

##Join different tables
set2 = (1, 2, 3, 4, 5, 6)
set = set.union(set2)
print(set)

##Add an element
set.add(100)
print(set)

##Delete an element
set.remove(100)

##Discard an element (if it is not inside the set, it happens nothing)
set.discard(400)

##Pop : deletes an aleatory value for the sets are not indexed
print(set.pop())

#Clear : empties all the set
print(set.clear())

"""
-------------- BOOLEAN --------------
"""

my_boolean = True



