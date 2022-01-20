"""
Los empleados reciben el 13% de comisión
Programa debe pedir nombre y cantidad vendida
Responderá con el nombre del empleado y con el resultado total que le debe percibir
"""

nombre = input("¿Cuál es tu nombre? ")
ventas = float(input("¿Cuál es la cantidad de ventas realizadas? "))

print(f"Gracias, {nombre}. El total a percibir correspondiente a las {ventas} ventas realizadas es de "
      f"{round(ventas*0.13, 2)}€.")