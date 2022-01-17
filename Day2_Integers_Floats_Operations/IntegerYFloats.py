"""
----------- VARIABLES -------------
"""
#Acepta variables de integer
mi_numero = "3"
print(type(mi_numero))
# ¡¡No puedes imprimir diferentes tipos de datos en el mismo print!!
print("Hola el numero es " + mi_numero)
#No es necesario indicar el tipo de valor que contendrá la variable y puede cambiarse, se debe hacer casting

"""
----------- CASTING -------------
"""

#Casting implícito: python convierte int a float
mi_numero = 3.24
print(mi_numero)

#Casting explícito: lo realizamos nosotros
print("Hola, el numero es" + str(mi_numero))

"""
----------- CONCATENACIÓN DE CADENAS [EVITAR CASTING INNECESARIO] -------------
"""
#Para evitar el casting, usaremos la concatenacion de cadenas
valor1 = 3.14
valor2 = "Shaila"
valor3 = 5
print("Hola, los valores son {}, {} y {}. La suma de los numeros es {}".format(valor1, valor2, valor3, valor3 + valor1))

#Posteriormente se implementó la concatenación de cadenas con las cadenas literales.
#Se debe poner "f" delante de la cadena literal, pero si no lo ponemos, python lo pondrá automáticamente
print(f"Hola, los valores son {valor1}, {valor2} y {valor3}. La suma de los números es {valor3 + valor1}")

"""
----------- OPERACIONES -------------
"""
x = 1
y = 2
z = 3

#Suma
print(x+y)
#Resta
print(y-x)
#Multiplicación
print(x*y*z)
#División SIN DECIMAL
print(z//y)
#División CON decimal
print(z/y)
#Resto de la división
print(z%y)
#Elevado a... [potencias]
print(z**y)
#Raíz cuadrada
print(f"La raíz cuadrada de {z} es {z**0.5}.")

#### REDONDEAR ####
print(round(z**0.5, 2)) #Cantidad de dígitos con el que queremos redondear))
print(round(z**0.5, 0))
print(type(round(z**0.5, 0)))
print(round(z**0.5)) #Si no indicamos el segundo parámetro, no mostrará ningun decimal
print(type(round(z**0.5))) # CAMBIA el tipo de valor