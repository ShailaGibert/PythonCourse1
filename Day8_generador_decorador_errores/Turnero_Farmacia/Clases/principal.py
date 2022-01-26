"""
Módulo en el que se genera un número de turno según el área pasada por el usuario
"""
from os import system

import generador_numeros


def bienvenida():
    """
    Módulo que imprime por pantalla el str inicial al correr el programa
    """
    print("Este es el generador de turno para la Farmacia Gibert.\n")


def opciones():
    print("A continuación le mostramos las áreas que puede escoger para pedir turno:\n"
          "[1]. FARMACIA\n"
          "[2]. PERFUMERIA\n"
          "[3]. COSMÉTICA\n")


def pedir_turno():
    """
    Se solicita un parámetro al usuario por consola
    :return: el parámetro casted a int
    """
    numero = int(input("Por favor, indique el número del área de la que desee solicitar turno: "))

    return numero


def turno_valido(numero):
    """
    Cuando el usuario indica un valor por consola, se confirma que esté dentro del rango(1, 4)
    :param numero:
    :return:
    """
    if numero in range(1, 4):
        return True
    print("***El valor introducido no corresponde a ningún área de la farmacia.***\n")
    input("Pulse cualquier tecla para continuar... ")
    #Limpiamos consola
    system('cls')
    return False


def turno_ok(numero):
    """
    Se confirma el input recibido por el usuario.
    :return: bool area_ok según el input del usuario.
    """
    areas = {1: "FARMACIA", 2: "PERFUMERIA", 3: "COSMÉTICA"}

    confirmacion = input(f"Ha introducido el área con número {areas[numero]}. ¿Es correcto? [S/N]: ").upper()

    correcto = {"S": True, "N": False}

    return correcto[confirmacion]


# Bucle infinito para el programa
while True:
    bienvenida()

    # Bucle para que cliente indique un número de área válido. Se repite mientras el código lance excepción
    while True:
        opciones()
        try:
            # Se solicita turno al usuario
            numero_turno = pedir_turno()

        except TypeError and ValueError:
            input("***Por favor, indique un número válido. Sólo debe indicar el número.***\n")

            #Limpiamos consola
            system('cls')
        else:
            #Si el usuario indica un valor válido de área [int]:
            if turno_valido(numero_turno):
                # Si el input es válido [ in range(1, 4)] , se sale del bucle
                break

    # Bucle para que cliente confirme con S/N si el número de área es correcto. Se repite hasta que usuario indica
    # un valor válido para la función turno_ok()
    while True:
        try:

            if turno_ok(numero_turno):  # Usuario indica S

                generador_numeros.frase_decoradora(numero_turno)
                parar_programa = input("Pulse cualquier tecla para continuar: ")

            else:  # Usuario indica N
                print(
                    "Se le llevará al menú principal para que pueda escoger de nuevo el número de área a la que desea "
                    "solicitar ticket")
                parar_programa = input("Pulse cualquier tecla para continuar: ")

        except ValueError and KeyError:
            print("*** El valor indicado no es válido. Por favor, indique S o N***\n")
        else:

            # Se limpia la consola
            system('cls')
            break
    # Manera de salir del bucle
    if parar_programa == "STOP":
        input("Gracias. Pulse cualquier tecla para salir... ")
        break
