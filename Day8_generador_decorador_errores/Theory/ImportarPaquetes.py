
# Para usar los módulos (archivo.py) y por tanto las funciones dentro de las mismas, deberemos importar el
# paquete en el que se encuentre

from Day8_generador_decorador_errores.Theory.Paquete1 import SumaYresta
from Day8_generador_decorador_errores.Theory.Paquete1.Subpaquete import Saludar

#Usamos los módulos de Paquete1
resultado_suma = SumaYresta.suma(2, 2)
resultado_resta = SumaYresta.resta(4, 2)
print(f"{resultado_suma}\n{resultado_resta}")

#Usamos los módulos de Paquete1.Subpaquete
print(Saludar.hey())
print(Saludar.hola())