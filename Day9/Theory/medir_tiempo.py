"""
--- TIME & TIMEIT ---
"""

# Nos sirve para medir la eficiencia de un código y la duración de ejecución de un programa
import time
import timeit


def prueba_for(numero):
    lista = []
    for num in range(1, numero + 1):
        lista.append(num)
    return lista


def prueba_while(numero):
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista


# Teniendo dos funciones que realizan lo mismo, gracias a time podremos saber cuanto tarda cada una en ejecutarse

inicio = time.time()
prueba_for(1000000)
final = time.time()
print(f"tiempo para for: {final - inicio}")

inicio = time.time()
prueba_while(1000000)
final = time.time()
print(f"Tiempo para while: {final - inicio}")

# Gracias a time, podemos confirmar que el for tarda menos que el while

# Cuando realizamos ejecuciones de funciones muy rápidas, usaremos timeit
# Deberemos separar las funciones en declaración y código
declaracion = '''
prueba_for(10)
'''

mi_setup = '''
def prueba_for(numero):
    lista = []
    for num in range(1, numero + 1):
        lista.append(num)
    return lista
'''

# declaración = función a llamar
# mi_setup =  código de la función llamada
# number = cantidad de veces que se repetirá este código
duracion = timeit.timeit(declaracion, mi_setup, number=99999999999999999)
print(f"Duración del for x 99999999999999999: {duracion}")

# Realizamos el mismo proceso para la segunda función
declaracion = '''
prueba_while(10)
'''

mi_setup = '''
def prueba_while(numero):
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista
'''

duracion = timeit.timeit(declaracion, mi_setup, number=99999999)
print(f"Duración del while x 99999999999999999: {duracion}")
