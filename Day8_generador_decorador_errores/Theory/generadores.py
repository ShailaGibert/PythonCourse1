"""
-- GENERADORES --
"""


# Nos entrega los valores ordenadamente según se le pide a la función.
# De esta manera ahorramos espacio del ordenador
# sustituimos el return por el yield

def mi_generador():
    yield 4
    # El generador está preparado para devolver este valor solo en caso que así se solicite


# Si imprimimos mi_generador, no nos habrá retornado nada
# Deberemos
print(next(mi_generador()))


# Si imprimimos este valor varias veces, dado que estará apuntando a un valor que no existe, nos lanzará error
# RECUERDA: SOLO LE HEMOS INDICADO QUE GENERE UN VALOR [4], POR LO TANTO SOLO UN NEXT

def loop_generador():
    for i in range(1, 6):
        # No es necesario guardar la lista, sino generar el valor
        yield i * 10


print("A continuación tendremos el cuadrado de los numeros del 1 al 5")
generador = loop_generador()
for i in range(1, 6):
    print(next(generador))


# Si existen varios yield en una función, la función se quedará en el último yield pasado y pasará al siguiente yield
# por cada next que llamemos

def suma_concatenada():
    x = 0
    while True:
        x += 1
        yield x


generador_suma = suma_concatenada()
for i in range(1, 100):
    print(next(generador_suma))
