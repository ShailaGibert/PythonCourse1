"""
El ahorcado
- Elige una palabra cn choice
- Contabiliza cantidad de letras y muestra guiones en su lugar
- Pide al usuario una letra
- Comprueba si la letra existe en la palabra y modifica los guiones por letras
- Tras realizar este proceso, confirma si el usuario ha acertado la palabra antes de que se le acaben las vidas
"""
from random import choice


def escoger_palabra(lista_palabras):
    palabra_escogida = choice(lista_palabras)
    return palabra_escogida

def contar_letras(palabra_escogida):
    palabra_en_guiones = ""
    for indicie in range(0, len(palabra_escogida)):
        palabra_en_guiones += "_"
    print("BIENVENIDO AL JUEGO DEL AHORCADO")
    print("********************************")
    print(f"La palabra que debes buscar contiene {len(palabra_escogida)} letras.")
    palabra_en_guiones = list(palabra_en_guiones)
    return (palabra_en_guiones)

def pedir_letra():
    letra = input("Indica una letra que la palabra pueda contener: ")
    return letra

def confirmar_letra_en_palabra(letra, palabra_escogida, palabra_en_guiones, vidas):
    palabra_escogida_list = list(palabra_escogida)
    ha_cambiado = False
    indice = 0
    for palabra in palabra_escogida_list:
        if palabra == letra:
            palabra_en_guiones[indice] = letra
            ha_cambiado = True
        indice += 1
    if ha_cambiado:
        print(f"¡Qué bien! Has acertado, la palabra contiene la letra {letra}.\n {palabra_en_guiones}")
    else:
        print(f"¡Mala suerte! La palabra no contiene la letra {letra}.\n {palabra_en_guiones}")
        vidas -= 1
    return vidas

def ha_acertado(palabra_escogida, palabra_en_guiones):
    palabra_escogida_list = list(palabra_escogida)
    if palabra_escogida_list == palabra_en_guiones:
        print(f"¡ENHORABUENA! Has acertado la palabra entera: \"{palabra_escogida}\"")
        return True
    return False

#Creamos la lista de palabras
lista_palabras = ['hola', 'shaila', 'prueba', 'alba', 'madre', 'python', 'trabajo']
#Escogemos una de las palabras de la lista aleatoriamente
palabra_escogida = escoger_palabra(lista_palabras)
#Contamos las letras e iniciamos juego
palabra_en_guiones = contar_letras(palabra_escogida)
print(palabra_en_guiones)
#Inicializamos vidas
vidas = 5

while vidas > 0:
    letra = pedir_letra()
    vidas = confirmar_letra_en_palabra(letra,palabra_escogida, palabra_en_guiones, vidas)
    print(f"Te quedan {vidas} vidas")
    es_ganador = ha_acertado(palabra_escogida, palabra_en_guiones)
    if es_ganador:
        break
if vidas == 0:
    print(f"¡MALA SUERTE! Te has quedado sin vidas. La palabra era {palabra_escogida}")
