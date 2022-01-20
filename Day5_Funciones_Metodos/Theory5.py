"""
---- AYUDA Y DOCUMENTACIÓN
"""
from random import shuffle, randint

diccionario = {'C1': 100, 'C2': 200, 'C3': 400}
print(diccionario.popitem())
print(diccionario.items())

frase = "hola mundoh pruebah"
frase2 = frase.lstrip("hola mundoh")
print(",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#".lstrip(",:_#,,,,,,:::____##"))
lista = ["banana", "piña"]
lista.insert(1, "naranja")

marcas_smartphone = {"Samsung", "Xiaomi", "Apple"}
marcas_tv = {"Sony", "Philips", "Samsung"}
print(marcas_tv.isdisjoint(marcas_smartphone))

"""
---- FUNCIONES -----
"""


# se crea con def
def primera_funcion():
    """
    Aquí va la explicación del fucionamiento de la función
    :return:
    """
    print("Se ha ejecutado primera_funcion")


primera_funcion()


def multiplicar(numero1, numero2):
    """
    Multiplica los valores pasados como argumento
    :param numero1:
    :param numero2:
    :return numero1 * numero2:
    """
    resultado = numero1 * numero2
    return resultado


resultado = multiplicar(3, 4)
print(f"El resultado de multiplicar 3 por 4 es {resultado}")

"""
--- FUNCIONES DINÁMICAS -----
"""


def confirmar_3_cifras(numero):
    """
    Revisa si el numero es de 3 cifras
    :param numero:
    :return:
    """
    return numero in range(100, 1000)


print(confirmar_3_cifras(345))

lista_numeros = [1, 50, 500, 5000, 750]


def suma_menores(lista_numeros):
    total = 0
    for numero in lista_numeros:
        if (numero > 0) and (numero < 100):
            total += numero
    return total


print(suma_menores(lista_numeros))

"""
--- DESEMPACAR TUPLES -----
"""

precios_cafe = [('solo', 2.30), ('mocca', 3.90), ('cafe con leche', 1.80)]

for cafe, precio in precios_cafe:
    print(cafe)
    print(precio)
    print("precio de compra " + str(precio * 0.45))  ## Precio de compra


def cafe_mas_caro(precios_cafe):
    precio_mayor = 0
    cafe_caro = ""
    for cafe, precio in precios_cafe:
        if precio > precio_mayor:
            precio_mayor = precio
            cafe_caro = cafe
    return cafe_caro, precio_mayor


cafe, precio = cafe_mas_caro(precios_cafe)
print(f"El cafe mas caro es el {cafe} que vale {precio} €")

"""
--- INTERACTUAR ENTRE FUNCIONES ---
"""

"""
ELIGE EL PALITO MÁS CORTO
1. Creamos lista inicial
2. Mezclamos palitos
3. Pedir a usuario que elija un palito que corresponderá a un numero
4. Función que comprobará si usuario ha elegido el palito más corto
"""


def mezclar(lista_a_mezclar):
    shuffle(lista_a_mezclar)
    return lista_a_mezclar


def pedir_numero():
    intento = 0
    while intento not in [1, 2, 3, 4]:
        intento = int(input("¡Te toca! Indica un número del 1 al 4: "))
    return intento


def comprobar_palito(lista, intento):
    if lista[intento - 1] == '-':
        print("¡Mala suerte! Has escogido el palito más corto.")
    else:
        print("¡Felicidades! No has elegido el palito más corto")


# Creamos lista inicial
palitos = ['-', '--', '---', '----']

# Mezclar palitos
palitos = mezclar(palitos)

# Pedir a usuario que elija un palito
intento = pedir_numero()

#Comprobar si usuario ha escogido el palito mas corto
comprobar_palito(palitos, intento)

print(randint(1, 7))

lista_numeros = [1, 2, 15, 7, 2]


def reducir_lista(lista_numeros):
    lista_numeros = set(lista_numeros)
    lista_numeros = list(lista_numeros)
    lista_numeros.sort()
    lista_numeros.pop(-1)
    return lista_numeros


def promedio(lista_numeros):
    suma = 0
    for numero in lista_numeros:
        suma += numero
    return suma / len(lista_numeros)


lista_numeros_reducidos = reducir_lista(lista_numeros)
total = promedio(lista_numeros_reducidos)
print(lista_numeros_reducidos)
print(total)

"""
---- *ARGS + **KWARGS -------
"""

#Sirve para poder indicar una cantidad indefinida de argumentos pasados por parámetro
def suma(*args):
    return sum(args)

print(suma(1,2))
print(suma(1,2,3))

#Con kwargs, tratamos con las palabras clave de un diccionario.
# Podemos acceder a ellos mediante la palabra clave que le indiquemos. Ej.: a = 1, b = 2, c = 3

def sumar(**kwargs):
    for clave, valor in kwargs.items():
        print(clave, valor)

sumar(x=1, y=2, z=3)

## Mezclar tipos de argumentos
def mostrar_en_pantalla(numero1, numero2, *args, **kwargs):
    print(f"El numero 1 es {numero1}")
    print(f"El numero 2 es {numero2}")
    for arg in args:
        print(f"arg = {arg}")
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

kwargs = {'color_ojos':'azul'}
mostrar_en_pantalla(1, 2, 3, 4, 5, **kwargs)
