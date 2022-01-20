"""
Escribe una función llamada contar_primos() que requiera un
solo argumento numérico.
Esta función va a mostrar en pantalla cuántos números
primos hay en el rango que va desde cero hasta ese número
incluido, y va a devolverla cantidad de números primos que
encontró.
Aclaración, por convención el 0 y el 1 no se consideran primos
"""


def contar_primos(numero):
    lista_numeros = list(range(2, numero + 1))
    numeros_primos = []
    contador = 0
    for numero in lista_numeros:
        es_primo = True
        for x in list(range(2, int(numero / 2))):
            if numero % x == 0:
                es_primo = False
        if es_primo:
            contador += 1
            numeros_primos.append(numero)
    print(numeros_primos)
    return contador


print(contar_primos(150))
