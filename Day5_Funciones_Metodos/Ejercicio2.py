"""
Escribe una función (puedes ponerle cualquier nombre que
quieras) que reciba cualquier palabra como parámetro, y que
devuelva todas sus letras únicas (sin repetir) pero en orden
alfabético.
Por ejemplo si al invocar esta función pasamos la palabra
"entretenido"
, debería devolver ['d','e','i','n','o','r','t']
"""
def letras_unicas(palabra):

    palabra = set(palabra)
    palabra = list(palabra)
    palabra.sort()
    return palabra

print(letras_unicas("entretenido"))