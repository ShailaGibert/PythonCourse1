"""
Módulo en el que se generan los números de las diferentes áreas
- Farmacia
- Perfumeria
- Cosmética
"""


def generador_farmacia():
    """
    función que genera un numero consecutivo desde el último generado
    :return: int numero generado
    """
    numero = 0
    while True:
        numero += 1
        yield f"FAR{numero}"


def generador_perfumeria():
    """
    función que genera un numero consecutivo desde el último generado
    :return: int numero generado
    """
    numero = 0
    while True:
        numero += 1
        yield f"PER{numero}"


def generador_cosmetico():
    """
    función que genera un numero consecutivo desde el último generado
    :return: int numero generado
    """
    numero = 0
    while True:
        numero += 1
        yield f"COS{numero}"


far = generador_farmacia()
per = generador_perfumeria()
cos = generador_cosmetico()


def frase_decoradora(area):
    """
    Función que envuelve los generadores en strings para evitar la duplicidad de los strings
    :param area: int pasado como argumento para conocer qué generador llamar
    """
    print("Se ha generado su número de turno correctamente:")
    match area:
        case 1:
            print(next(far))
        case 2:
            print(next(per))
        case 3:
            print(next(cos))
    print("Espere a que el número de su ticket aparezca en la pantalla superior.")
    print("Gracias\n\n")

