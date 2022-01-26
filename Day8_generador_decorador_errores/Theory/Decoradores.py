"""
---- DECORADORES ----
"""


# No solo existen los decoradores creados por Python, sino que nosotros también podemos crear decoradores
# Los decoradores nos ayudan a modificar el comportamiento de una función al llamarla

def mayus(texto):
    print(texto.upper())


def minus(texto):
    print(texto.lower())


# Dado que python está orientado a objetos, las variables y las funciones son objetos
# Por lo tanto podemos asignar a una variable una función
# mi_variable = mayus("texto")


# Así pues, podemos también pasar una función como argumento de otra función
def mi_funcion(funcion):
    return funcion


# mi_funcion(mi_variable)
# Equivale a:
# mi_funcion(mayus("texto"))


# También podemos definir funciones dentro de funciones
def cambiar_letra(tipo):
    def mayuscula(argumento):
        print(argumento.upper())
        return argumento.upper()

    def minuscula(argumento):
        print(argumento.lower())
        return argumento.lower()

    match tipo:
        case 'may':
            return mayuscula
            # Cuando se retorna una función, NO se pasan los argumentos y por lo tanto no hacen falta los paréntesis
        case 'min':
            return minuscula


mi_operacion = cambiar_letra('may')
# mi_operacion('texto')


# print(texto)


# Una vez entendido este concepto, podemos entender los decoradores:

# Esta función es en la que envolveremos la función en cuestión cuando queramos usarla
def decorador_saludo(funcion):
    def funcion_decorada(palabra):
        print("hola")
        funcion(palabra)
        print("adios")

    return funcion_decorada


print(f"Esto es una prueba con operacion")
cambiar_letra('may')('esto es una prueba')


print(f"\nEsto es una prueba con operacion_decorada =")
decorador_saludo(mayus)('esto es una prueba') #Mayus no devuelve nada

print(f"\nEsto es una segunda prueba con operacion_decorada =")
funcion = cambiar_letra('may')
decorador_saludo(funcion)('esto es una prueba')

# Aquí guardamos el retorno de la función. ¡OJO! Es un str, por lo que NO es una función!!!!
retorno_funcion = cambiar_letra('may')('la ultima prueba')
print(f"\nEsta es la ÚLTIM prueba con operacion_decorada = {retorno_funcion}")
