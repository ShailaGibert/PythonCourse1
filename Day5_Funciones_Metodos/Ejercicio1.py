"""
Crea una función llamada devolver_distintos() que reciba 3
integers como parámetros.
Si la suma de los 3 numeros es mayor a 15, va a devolver el
número mayor.
Si la suma de los 3 numeros es menor a 10, va a devolver el
número menor.
Si la suma de los 3 números es un valor entre 10 y 15
(incluidos) va a devolver el número de valorintermedio
"""
def devolver_distintos(numero1, numero2, numero3):
    suma = numero1 + numero2 + numero3
    if suma > 15:
        return max(numero1, numero2, numero3)
    elif suma < 10:
        return min(numero1, numero2, numero3)
    else:
        return suma/3

print(devolver_distintos(1, 2, 3))