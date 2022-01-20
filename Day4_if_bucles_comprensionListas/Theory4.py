from random import randint, uniform, choice, shuffle

"""
------- COMPARADORES -------
"""
control = 10 == 30
print(control)
print(10 != 20)
##Podemos comparar strings directamente, CASE SENSITIVE
print('blanco' == 'Blanco')
print('blanco' == 'blanco')
print('blanco'.lower() == 'BLANCO'.lower())
#Podemos usar operadores de comparación con diferentes tipos de datos
print(10.0 == 10)

##OPERADORES LÓGICOS [and, or, not]

print(4 < 5 and 5 < 6)
print (4 == 4 or 3 == 4 )
frase = "Frase de prueba"
print(("Frase" in frase)) and ('prueba' in frase)
print(not(4 == 4)) ##Doble negación, muestra el resultado contrario a la comparación

"""
---------- CONTROL DE FLUJO -----------
"""

## IF/ELIF/ELSE
edad = 67
if edad < 18:
    print("Eres menor de edad")
elif (edad > 18) and (edad < 67):
    print("Eres adulto pero no estas jubilado")
elif (edad >= 67) and (edad < 110):
    print("Ya estás jubilado")
else:
    print("La edad introducida no es valida")


"""
------ ITERACIONES --------
"""

## FOR
lista = ['A', 'B', 'C']
for letra in lista:
    print(f"La letra leída es {letra} y está en la posición {lista.index(letra) + 1}")

lista2 = ["Shaila", "Paquita", "Josep Maria"]
for nombre in lista2:
    if nombre.startswith('S'):
        print (f"El nombre empieza con S. El nombre en concreto es {nombre}")
    else:
        print(f"El nombre {nombre} no empieza con \"S\"")
diccionario = {'clave1':'Shaila', 'clave2':'Gibert', 'clave3':'Marco'}
for clave in diccionario:
    print(clave)
for clave in diccionario.items():
    print(clave)

#Si agregamos varias variables al bucle, cada variable se quedará con un valor
for a, b, c in [[1, 2, 3], [1, 2, 3], [3, 2, 1]]:
    print(a, b, c)
    print(a)
    print(b)
    print(c)

##WHILE
monedas = 5;
while monedas > 0:
    print(f"Tengo {monedas} monedas")
    monedas -= 1
## Podemos integrar un else para cuando no se cumpla la condición del while
else: print("No tengo más monedas")

## PASS
##while monedas == 0:
    ##pass ## Cuando queremos mantener un bucle pero que no haga nada (por ahora)

monedas = 100;
while monedas != 0:
    if monedas == 1:
        print("Te queda solo 1 moneda, no te la gastes.")
        break ##Pausa el bucle
    if monedas  == 100:
        print("Tienes el máximo de monedas")
        monedas -= 1
        continue ##Realiza una accion fuera de la norma del bucle pero hace que el bucle continue
    print(f"Tienes {monedas} monedas")
    monedas -= 1

"""
---- RANGO ------
"""

#Función que te permite establecer un rango de numeros sin crear una lista ni cualquier elemento iterable como tal

#Se puede usar en la creación de cualquier lista, tupla etc que deba ser ordenada

lista = list(range(0, 11)) ## DEBE SER CASTEADO DE RANGO A LISTA

for numero in lista:
    print(numero)
for numero in range(6): #Itinera del 0 al 5 SIN incluir el último
    print(numero)
for numero in range(50, 101):
    print(numero)
for numero in range(0, 101, 2): ##Qué salto realiza
    print (numero)

## ENUMERATOR : sirve para indicar el indice del valor dentro de una lista en una tupla
lista = ['a', 'b', 'c']


for indice, item in  enumerate(lista):
    print(indice, item)

"""
------ ZIP ----------
"""

#une varias listas/diccionarios etc en tuples. LLEGA HASTA EL LARGO DE LA LISTA MAS CORTA

nombre = ['Shaila', 'Paquita', 'Josep']
edades= [20, 61, 62]

# Se debe castear a lista para que se pueda mostrar el contenido

cominado = list(zip(nombre, edades))

"""
------- MIN & MAX -----
"""

# Revisar el mínimo o maximo de unos valores dados o bien de una coleccion iterable

print(min(1, 2, 3, 4))
print(max(1, 2, 3, 4))

##Revisará por orden alfabético. CASE SENSITVE
lista = ["shaila", 'shailb']
print(min(lista))
print(max(lista))
print(min("Shaila"))
print(min("shaila"))

## MIN y MAX con diccionario
##Nos dirá la clave más pequeña o mayor
diccionario = {'clave1':12, 'clave2' :11}
print(min(diccionario))

# Nos dirá el VALOR más pequeño o mayor si indicamos .values()
print(min(diccionario.values()))
print(min(diccionario.items()))

"""
------- RANDOM ----------
"""
# Randint : nuemro entero aleatorio entre un rango
aleatorio = randint(1, 50)
print (aleatorio)

#Uniform : valor aleatorio DECIMAL. SE PUEDE REDONDEAR EL FLOAT
aleatorio = uniform(1, 50)
print(aleatorio)

# Choice : elige un valor de un coleccionable
aleatorio = ['blanco', 'negro', 'rojo']
print(choice(aleatorio))

#Shuffle : mezcla un coleccionable de manera aleatoria
shuffle(aleatorio)
print(aleatorio)

"""
------ COMPRENSION DE LISTAS
"""

palabra = 'python'
lista

for letra in palabra:
    lista.append(letra)

## PODEMOS OPTIMIZAR ESTE PROCESO POR UNA COPMRENSION DE LISTAS

lista = [letra for letra in palabra]
print(lista)

# Se pueden añadir condiciones u operaciones
lista = [numero/2 if numero%2 == 0 else numero for numero in range(0, 21)]
print(lista)

medidas_en_pies = range(10, 101, 10)
medidas_en_metros = [pies * 3.281 for pies in medidas_en_pies]
print(medidas_en_metros)

"""
--- MATCH ---
"""

cliente = {"Nombre": "Shaila", "Edad":21, "Ocupacion": "estudiante"}
pelicula = {"titulo":"Hola", "Casting": {"Actor": "Keanu Reeves", "Director":"Shaila Gibert"}, "Genero": "Drama"}
elementos = [cliente, pelicula]

for elemento in elementos:
    match elemento:
        case {"Nombre": nombre, "Edad": edad, "Ocupacion": ocupacion}:
            print(f"Es un cliente. Concretamente: {elemento}")
        case{"titulo":titulo, "Casting":{"Actor":actor, "Director":director}, "Genero": genero}:
            print(f"Es una pelicula. Concretamente: {elemento}")

