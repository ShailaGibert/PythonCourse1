"""
---- MANEJO DE ERRORES ----
"""


# Nos sirve para que ante una excepción, el código no pare

# try --> intenta esto
# except --> si lo que hay en try no sale, haz esto
# finally --> pase lo que pase, si pasas a try o a except, haz esto
from os import system


def suma():
    # Pedimos valores a usuario
    x = int(input("Ingrese primer numero a sumar: "))
    y = int(input("Ingrese segundo numero a sumar: "))
    return x + y


# Si el usuario indicara un valor no casteable a integer, nos saltará error
try:
    # Código que queremos probar
    suma_total = suma()
except:
    # Código a ejecutar si hay error en try
    print("Algo no ha salido bien...")
else:
    # Código a ejecutar si NO hay un error
    print("Gracias por sumar")
    try:
        # Al concatenar str y int, el error que nos salta es el TypeError. Puedes "catch" errores concretos
        print("El resultado de la suma es" + suma_total)
    except TypeError:
        print("Estás intentando concatenar tipos de datos distintos. Vamos a castearlos...")
        print(f"El resultado de la suma es {suma_total}")

finally:
    # Código que se va a ejecutar siempre
    input("Orden finalizada. Pulse cualquier tecla para continuar... ")
    system('cls')

def pedir_numero():
    while True:
        try:
            numero = int(input("Dame un numero: "))
        except:
            print("El valor introducido no es válido.")
        else:
            print(f"El número introducido es el {numero}")
            break
    input("Gracias por usar nuestra función. Presione cualquier tecla para continuar: ")

pedir_numero()
