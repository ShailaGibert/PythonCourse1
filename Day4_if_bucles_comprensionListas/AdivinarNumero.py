from random import randint

"""
ADIVINAR NÚMERO
Pide nombre al cliente
Usuario tiene 8 oportunidades
Si el usuario indica un numero menor a 1 o superior a 100 --> numero no permitido
Numero menor al secreto --> se informa
Numero mayor al secreto --> se informa
Cuando adivine el numero, se informa al cliente y se le indica la cantidad de veces que ha tenido que intentarlo
"""

nombre = input("¡Bienvenido al juego \"Adivina el número\"! En primer lugar, ¿cuál es tu nombre?\n")
numero_secreto = randint(1,101)
vidas = 8
while vidas > 0:
    numero_indicado = int(input("¿Qué número cree que es el indicado?\n"))
    if numero_indicado == numero_secreto:
        print(f"¡Felicidades {nombre}! Ha conseguido acertar el número secreto."
              f" Ha acertado en el intento número {8 - vidas}\n")
        break
    elif (numero_indicado < 1) or (numero_indicado > 100):
        print("El numero indicado no es valido. Recuerde que debe ser un numero comprendido enter el 1 y el 100.\n"
              "No se le restarán vidas por este intento.")
    elif (numero_indicado > numero_secreto):
        if vidas == 1:
            print(f"Lo sentimos. No ha conseguido acertar el número secreto. Era el {numero_secreto}. "
                  f"¡Pruebe de nuevo!\n")
            break
        print("El numero indicado no es el número secreto. Pista: ha indicado un número MAYOR que el número secreto. "
              f"Le quedan {vidas -1} intentos")
        vidas -=1
    elif (numero_indicado < numero_secreto):
        if vidas == 1:
            print(f"Lo sentimos. No ha conseguido acertar el número secreto. Era el {numero_secreto}. "
                  f"¡Pruebe de nuevo!\n")
            break
        print("El número indicado no es el número secreto. Pista: ha indicado un número MENOR que el número secreto. "
              f"Le quedan {vidas-1} intentos")
        vidas -=1
    else:
        print("Ha ocurrido un error con el juego. Por favor, inténtelo de nuevo.")
        break